import sys

from pathlib import Path



sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))



from assistant import anomaly_signals, build_report, inventory_forecast





def test_anomaly_signals_flag_large_payment():
  
    rows = [
      
        {"transaction_id": "A", "amount": "100"},
      
        {"transaction_id": "B", "amount": "110"},
      
        {"transaction_id": "C", "amount": "105"},
      
        {"transaction_id": "D", "amount": "1000"},
      
    ]
  
    flagged = anomaly_signals(rows)
  
    assert [row["transaction_id"] for row in flagged] == ["D"]
  




def test_inventory_forecast_recommends_reorder():
  
    rows = [
      
        {"item": "Sensor", "stock": "10", "average_daily_sales": "2", "reorder_point_days": "7"},
      
        {"item": "Cable", "stock": "100", "average_daily_sales": "2", "reorder_point_days": "7"},
      
    ]
  
    forecast = inventory_forecast(rows)
  
    assert forecast[0]["needs_reorder"] is True
  
    assert forecast[1]["needs_reorder"] is False
  




def test_report_contains_recommendations():
  
    transactions = [{"transaction_id": "A", "amount": "100"}]
  
    inventory = [{"item": "Sensor", "stock": "2", "average_daily_sales": "1", "reorder_point_days": "7"}]
  
    report = build_report(transactions, inventory)
  
    assert report["summary"]["total_transactions"] == 1
  
    assert report["recommendations"]
  























