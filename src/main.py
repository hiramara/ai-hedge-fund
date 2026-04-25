"""AI Hedge Fund - Main Entry Point

This module serves as the primary entry point for the AI Hedge Fund application.
It orchestrates the various agents and workflows for automated trading analysis.
"""

import argparse
import sys
from datetime import datetime, timedelta

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments for the hedge fund runner."""
    parser = argparse.ArgumentParser(
        description="AI Hedge Fund - Automated trading analysis using LLM agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/main.py --ticker AAPL
  python src/main.py --ticker TSLA --start-date 2024-01-01 --end-date 2024-06-01
  python src/main.py --ticker NVDA --show-reasoning
        """,
    )

    parser.add_argument(
        "--ticker",
        type=str,
        required=True,
        help="Stock ticker symbol to analyze (e.g., AAPL, TSLA, NVDA)",
    )
    parser.add_argument(
        "--start-date",
        type=str,
        default=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        help="Start date for analysis in YYYY-MM-DD format (default: 90 days ago)",
    )
    parser.add_argument(
        "--end-date",
        type=str,
        default=datetime.now().strftime("%Y-%m-%d"),
        help="End date for analysis in YYYY-MM-DD format (default: today)",
    )
    parser.add_argument(
        "--show-reasoning",
        action="store_true",
        default=False,
        help="Display the reasoning process of each agent",
    )
    parser.add_argument(
        "--initial-capital",
        type=float,
        default=100_000.0,
        help="Initial capital for portfolio simulation (default: $100,000)",
    )

    return parser.parse_args()


def validate_date(date_str: str) -> bool:
    """Validate that a date string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main() -> None:
    """Main function to run the AI Hedge Fund analysis pipeline."""
    args = parse_arguments()

    # Validate date inputs
    if not validate_date(args.start_date):
        print(f"Error: Invalid start date format '{args.start_date}'. Use YYYY-MM-DD.")
        sys.exit(1)

    if not validate_date(args.end_date):
        print(f"Error: Invalid end date format '{args.end_date}'. Use YYYY-MM-DD.")
        sys.exit(1)

    start_dt = datetime.strptime(args.start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(args.end_date, "%Y-%m-%d")

    if start_dt >= end_dt:
        print("Error: start-date must be before end-date.")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  AI Hedge Fund Analysis")
    print(f"{'='*60}")
    print(f"  Ticker:          {args.ticker.upper()}")
    print(f"  Period:          {args.start_date} to {args.end_date}")
    print(f"  Initial Capital: ${args.initial_capital:,.2f}")
    print(f"  Show Reasoning:  {args.show_reasoning}")
    print(f"{'='*60}\n")

    # TODO: Initialize and run the agent workflow
    # from src.agents.workflow import run_hedge_fund
    # result = run_hedge_fund(
    #     ticker=args.ticker.upper(),
    #     start_date=args.start_date,
    #     end_date=args.end_date,
    #     portfolio={"cash": args.initial_capital, "stock": 0},
    #     show_reasoning=args.show_reasoning,
    # )
    # print(result)

    print("Pipeline initialization complete. Agent workflow coming soon.")


if __name__ == "__main__":
    main()
