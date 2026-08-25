from pathlib import Path

import sys



sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))



from assistant import anomaly_signals, build_report, inventory_forecast





def main():
  
    rows = [
      
        {"transaction_id": "A", "amount": "100"},
      
        {"transaction_id": "B", "amount": "110"},
      
        {"transaction_id": "C", "amount": "105"},
      
        {"transaction_id": "D", "amount": "1000"},
      
    ]
  
    assert [row["transaction_id"] for row in anomaly_signals(rows)] == ["D"]
  


    inventory = [
      
        {"item": "Sensor", "stock": "10", "average_daily_sales": "2", "reorder_point_days": "7"},
      
        {"item": "Cable", "stock": "100", "average_daily_sales": "2", "reorder_point_days": "7"},
      
    ]
  
    forecast = inventory_forecast(inventory)
  
    assert forecast[0]["needs_reorder"] is True
  
    assert forecast[1]["needs_reorder"] is False
  


    report = build_report([{"transaction_id": "A", "amount": "100"}], inventory[:1])
  
    assert report["summary"]["total_transactions"] == 1
  
    assert report["recommendations"]
  
    print("All prototype checks passed.")
  




if __name__ == "__main__":
  
    main()
  





















