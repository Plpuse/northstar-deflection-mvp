# Go-Live Readiness Note

**Project:** Northstar Deflection MVP
**Purpose:** Automated support-deflection tool handling order-status, returns, and stock-availability questions for customers.
**Status date:** 2026-08-15

## What Works

### Order Status Lookup (`src/order_lookup.py`)
Looks up an order by ID in `data/orders.json` and returns its status and item name. Tested manually against order 1001 (Wireless Mouse, Shipped). Handles missing files and malformed JSON gracefully. No CLI wrapper yet - runs as a script with a hardcoded test ID.

### Return Policy Engine (`src/return_policy.py`)
Decision-tree logic that determines return eligibility based on days since delivery, item condition, return reason, and final-sale status. Covers 4 scenarios: normal return, late return, damaged/defective item, and final-sale rejection. Has built-in test cases in its `main()` function covering all 4 paths. No CLI wrapper yet.

### Stock Lookup (`src/stock_lookup.py` + `src/stock_cli.py`)
Given a SKU, returns whether it's in stock and the quantity, reading from `data/stock.json`. Now has an interactive command-line interface (`stock_cli.py`) so a user can type a SKU and get a plain-English response. Manually tested against 3 SKUs: in-stock, out-of-stock, and not-found - all returned correct results.

## Known Issues / Not Yet Done

- **No unified interface.** Only stock lookup has a CLI wrapper (issue #8). Order status and returns still run as standalone scripts with hardcoded test data, not interactive tools.
- **Stray data file.** `data/orders.json,` (note the trailing comma in the filename) exists in the `data` folder but is not used by any code - it has a different structure and different sample data than the real `data/orders.json`. This looks like a leftover mistake and should be deleted or investigated.
- **No automated test suite.** All testing so far is manual, via each script's `main()` function or manual CLI runs. There is no `pytest` or similar automated test coverage.
- **Sample data only.** All data files (`orders.json`, `stock.json`) contain small hand-written sample datasets, not a connection to any real order or inventory system.

## What the Client's Team Needs to Know

- **Project layout:** All logic lives in `src/`, all sample data lives in `data/`, both as flat JSON files read directly by each script.
- **Running the tools today:** Each script can be run directly with `python src/<script_name>.py` from the repo root (paths inside the scripts are relative to the root, not to `src/`).
- **No web/chat interface exists yet.** Everything is a command-line script or importable Python module - there is no dashboard, API, or chat integration in this MVP.
- **Before going further:** the client's team should prioritize (1) resolving the stray `orders.json,` file, (2) deciding whether order-status and returns need CLI wrappers like stock lookup got, and (3) replacing sample JSON data with a connection to their real systems.
