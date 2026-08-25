# AI-Powered IoT Payment and Inventory Assistant

A prototype for the **Razorpay AI Builder Internship 2026 – Open Track**.

This project is designed for small businesses that need a simple way to understand payment activity, monitor inventory, detect unusual transactions, and receive actionable recommendations without a dedicated data or finance team.

## Project objectives

The assistant analyzes transaction and inventory data to identify unusual payment patterns, estimate when products may need replenishment, and produce concise business recommendations. The long-term vision is to connect the analytics layer to an ESP32 or ARM-based edge device that can display alerts locally while synchronizing summaries to a cloud dashboard.

## Why this fits the Open Track

The project combines:

- **Fintech:** payment summaries, transaction monitoring, cash-flow visibility, and fraud-awareness signals.
- **AI/analytics:** anomaly detection, demand estimation, and natural-language recommendations.
- **Embedded systems:** an intended edge-device interface using ESP32/ARM microcontrollers and sensor or display modules.
- **Small-business impact:** practical alerts that help reduce stock-outs and improve day-to-day decisions.

## Current prototype

The current implementation is an offline, explainable analytics demo. It reads sample transaction and inventory data, calculates daily payment totals, flags unusual transaction amounts using a robust median/MAD rule, estimates days of inventory remaining, and creates a JSON report with recommended actions.

It intentionally does **not** connect to live Razorpay accounts or process real payments. No API keys or sensitive customer data are required.

## Architecture

```text
CSV transaction and inventory data
              |
              v
      Analytics engine (Python)
       |       |        |
       v       v        v
 Payment   Anomaly   Inventory
 summary   signals   forecast
              |
              v
      Recommendations JSON
              |
              v
 Future ESP32/ARM display or web dashboard
```

## Run locally

The prototype uses only the Python standard library.

```bash
python3 src/assistant.py --transactions data/transactions.csv --inventory data/inventory.csv --output report.json
```

The generated `report.json` contains payment summaries, flagged transactions, inventory projections, and recommended actions.

## Example output

```json
{
  "summary": {
    "total_transactions": 12,
    "total_amount": 54000.0,
    "average_transaction": 4500.0
  },
  "recommendations": [
    "Review flagged transaction TXN-011 for unusual amount.",
    "Reorder Wireless Sensor Kit: estimated stock cover is below 7 days."
  ]
}
```

## Roadmap

1. Add a secure Razorpay payment-data connector using official APIs and environment variables.
2. Add a lightweight dashboard for business owners.
3. Add an ESP32/ARM companion device with an OLED display, buzzer, and Wi-Fi/MQTT communication.
4. Replace the baseline demand estimator with a validated forecasting model after collecting sufficient historical data.
5. Add role-based access, consent management, audit logging, and production-grade security.

## Skills demonstrated

**Python, Embedded Systems, ESP32/ARM planning, IoT architecture, data analysis, anomaly detection, inventory logic, JSON APIs, MQTT-ready design, and technical documentation.**

## Author

**Bhargavi Madipelly**  
M.Tech Embedded Systems  
Hyderabad, India
