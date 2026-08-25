"""Explainable payment and inventory assistant prototype.



This offline demo uses CSV files and the Python standard library only.

It does not connect to live payment accounts or handle sensitive data.

"""



from __future__ import annotations



import argparse

import csv

import json

import statistics

from datetime import datetime, timezone

from pathlib import Path

from typing import Any





def read_csv(path: Path) -> list[dict[str, str]]:
  
    with path.open(newline="", encoding="utf-8") as handle:
      
        return list(csv.DictReader(handle))
      




def as_float(value: str) -> float:
  
    return float(value.strip())
  




def payment_summary(transactions: list[dict[str, str]]) -> dict[str, float | int]:
  
    amounts = [as_float(row["amount"]) for row in transactions]
  
    return {
      
        "total_transactions": len(amounts),
      
        "total_amount": round(sum(amounts), 2),
      
        "average_transaction": round(statistics.mean(amounts), 2) if amounts else 0.0,
      
        "largest_transaction": round(max(amounts), 2) if amounts else 0.0,
      
    }
  




def anomaly_signals(transactions: list[dict[str, str]]) -> list[dict[str, Any]]:
  
    """Flag unusually large transactions with a robust median/MAD rule."""
  
    if not transactions:
      
        return []
      


    amounts = [as_float(row["amount"]) for row in transactions]
  
    median = statistics.median(amounts)
  
    deviations = [abs(amount - median) for amount in amounts]
  
    mad = statistics.median(deviations)
  
    threshold = median + (6 * mad if mad else max(median * 1.5, 1.0))
  


    flagged: list[dict[str, Any]] = []
  
    for row, amount in zip(transactions, amounts):
      
        if amount > threshold:
          
            flagged.append(
              
                {
                  
                    "transaction_id": row["transaction_id"],
                  
                    "amount": round(amount, 2),
                  
                    "reason": "Amount is unusually high compared with the transaction baseline.",
                  
                    "review_required": True,
                  
                }
              
            )
          
    return flagged
  




def inventory_forecast(inventory: list[dict[str, str]]) -> list[dict[str, Any]]:
  
    results: list[dict[str, Any]] = []
  
    for row in inventory:
      
        stock = as_float(row["stock"])
      
        daily_sales = as_float(row["average_daily_sales"])
      
        days_left = stock / daily_sales if daily_sales > 0 else None
      
        reorder_point = as_float(row["reorder_point_days"])
      
        needs_reorder = days_left is not None and days_left <= reorder_point
      
        results.append(
          
            {
              
                "item": row["item"],
              
                "stock": round(stock, 2),
              
                "estimated_days_remaining": round(days_left, 1) if days_left is not None else None,
              
                "reorder_point_days": round(reorder_point, 1),
              
                "needs_reorder": needs_reorder,
              
            }
          
        )
      
    return results
  




def build_report(transactions: list[dict[str, str]], inventory: list[dict[str, str]]) -> dict[str, Any]:
  
    flagged = anomaly_signals(transactions)
  
    forecast = inventory_forecast(inventory)
  
    recommendations = [
      
        f"Review flagged transaction {item['transaction_id']} for unusual amount."
      
        for item in flagged
      
    ]
  
    recommendations.extend(
      
        f"Reorder {item['item']}: estimated stock cover is below {item['reorder_point_days']:g} days."
      
        for item in forecast
      
        if item["needs_reorder"]
      
    )
  
    if not recommendations:
      
        recommendations.append("No immediate payment anomaly or inventory reorder signal detected.")
      


    return {
      
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
      
        "summary": payment_summary(transactions),
      
        "anomalies": flagged,
      
        "inventory_forecast": forecast,
      
        "recommendations






































































