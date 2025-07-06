#!/usr/bin/env python3
"""
Python Data Analysis Example
This demonstrates how to analyze data using only built-in Python features.
No external libraries required!
"""

import json
import csv
from datetime import datetime, timedelta
import random

def generate_sample_data():
    """Generate sample sales data for demonstration"""
    print("Generating sample sales data...")
    
    # Sample data
    products = ["Laptop", "Phone", "Tablet", "Headphones", "Mouse", "Keyboard"]
    salespeople = ["Alice Johnson", "Bob Smith", "Carol Davis", "David Wilson", "Eve Brown"]
    
    sales_data = []
    
    # Generate 50 random sales records
    for i in range(50):
        # Random date within last 30 days
        days_ago = random.randint(0, 30)
        sale_date = datetime.now() - timedelta(days=days_ago)
        
        sale = {
            "id": i + 1,
            "date": sale_date.strftime("%Y-%m-%d"),
            "product": random.choice(products),
            "salesperson": random.choice(salespeople),
            "quantity": random.randint(1, 5),
            "unit_price": round(random.uniform(50, 1000), 2),
            "customer_rating": random.randint(1, 5)
        }
        
        # Calculate total
        sale["total"] = round(sale["quantity"] * sale["unit_price"], 2)
        sales_data.append(sale)
    
    return sales_data

def save_data_to_csv(data, filename):
    """Save data to CSV file"""
    if not data:
        return
    
    # Get column headers from first record
    headers = data[0].keys()
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data saved to {filename}")

def load_data_from_csv(filename):
    """Load data from CSV file"""
    data = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert numeric fields
                row['id'] = int(row['id'])
                row['quantity'] = int(row['quantity'])
                row['unit_price'] = float(row['unit_price'])
                row['total'] = float(row['total'])
                row['customer_rating'] = int(row['customer_rating'])
                data.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found")
    
    return data

def analyze_sales_data(sales_data):
    """Perform comprehensive analysis on sales data"""
    if not sales_data:
        print("No data to analyze")
        return
    
    print("\n" + "="*50)
    print("SALES DATA ANALYSIS")
    print("="*50)
    
    # 1. Basic Statistics
    print("\n1. BASIC STATISTICS")
    print("-" * 25)
    
    total_sales = sum(sale['total'] for sale in sales_data)
    total_quantity = sum(sale['quantity'] for sale in sales_data)
    num_transactions = len(sales_data)
    avg_transaction = total_sales / num_transactions if num_transactions > 0 else 0
    
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Quantity Sold: {total_quantity}")
    print(f"Number of Transactions: {num_transactions}")
    print(f"Average Transaction Value: ${avg_transaction:.2f}")
    
    # 2. Product Analysis
    print("\n2. PRODUCT ANALYSIS")
    print("-" * 25)
    
    product_stats = {}
    for sale in sales_data:
        product = sale['product']
        if product not in product_stats:
            product_stats[product] = {
                'quantity': 0,
                'revenue': 0,
                'transactions': 0
            }
        
        product_stats[product]['quantity'] += sale['quantity']
        product_stats[product]['revenue'] += sale['total']
        product_stats[product]['transactions'] += 1
    
    # Sort by revenue
    sorted_products = sorted(product_stats.items(), 
                           key=lambda x: x[1]['revenue'], 
                           reverse=True)
    
    print("Top Products by Revenue:")
    for product, stats in sorted_products:
        print(f"  {product}: ${stats['revenue']:,.2f} "
              f"({stats['quantity']} units, {stats['transactions']} transactions)")
    
    # 3. Salesperson Performance
    print("\n3. SALESPERSON PERFORMANCE")
    print("-" * 35)
    
    salesperson_stats = {}
    for sale in sales_data:
        person = sale['salesperson']
        if person not in salesperson_stats:
            salesperson_stats[person] = {
                'revenue': 0,
                'transactions': 0,
                'total_rating': 0
            }
        
        salesperson_stats[person]['revenue'] += sale['total']
        salesperson_stats[person]['transactions'] += 1
        salesperson_stats[person]['total_rating'] += sale['customer_rating']
    
    # Calculate averages and sort
    for person in salesperson_stats:
        stats = salesperson_stats[person]
        stats['avg_rating'] = stats['total_rating'] / stats['transactions']
    
    sorted_salespeople = sorted(salesperson_stats.items(), 
                              key=lambda x: x[1]['revenue'], 
                              reverse=True)
    
    print("Salesperson Performance:")
    for person, stats in sorted_salespeople:
        print(f"  {person}: ${stats['revenue']:,.2f} "
              f"({stats['transactions']} sales, "
              f"avg rating: {stats['avg_rating']:.1f})")
    
    # 4. Time-based Analysis
    print("\n4. TIME-BASED ANALYSIS")
    print("-" * 30)
    
    daily_sales = {}
    for sale in sales_data:
        date = sale['date']
        if date not in daily_sales:
            daily_sales[date] = 0
        daily_sales[date] += sale['total']
    
    # Sort dates
    sorted_dates = sorted(daily_sales.items())
    
    print("Daily Sales (last 10 days):")
    for date, revenue in sorted_dates[-10:]:
        print(f"  {date}: ${revenue:,.2f}")
    
    # 5. Customer Rating Analysis
    print("\n5. CUSTOMER SATISFACTION")
    print("-" * 30)
    
    rating_counts = {}
    total_ratings = 0
    for sale in sales_data:
        rating = sale['customer_rating']
        rating_counts[rating] = rating_counts.get(rating, 0) + 1
        total_ratings += rating
    
    avg_rating = total_ratings / len(sales_data)
    
    print(f"Average Customer Rating: {avg_rating:.2f}/5")
    print("Rating Distribution:")
    for rating in sorted(rating_counts.keys()):
        count = rating_counts[rating]
        percentage = (count / len(sales_data)) * 100
        print(f"  {rating} stars: {count} ({percentage:.1f}%)")
    
    # 6. Advanced Analytics
    print("\n6. ADVANCED INSIGHTS")
    print("-" * 25)
    
    # Find best and worst performing days
    if daily_sales:
        best_day = max(daily_sales.items(), key=lambda x: x[1])
        worst_day = min(daily_sales.items(), key=lambda x: x[1])
        print(f"Best sales day: {best_day[0]} (${best_day[1]:,.2f})")
        print(f"Worst sales day: {worst_day[0]} (${worst_day[1]:,.2f})")
    
    # High-value transactions
    high_value_sales = [sale for sale in sales_data if sale['total'] > avg_transaction * 1.5]
    print(f"High-value transactions (>${avg_transaction * 1.5:.2f}+): {len(high_value_sales)}")
    
    # Product with highest customer satisfaction
    product_ratings = {}
    for sale in sales_data:
        product = sale['product']
        if product not in product_ratings:
            product_ratings[product] = []
        product_ratings[product].append(sale['customer_rating'])
    
    product_avg_ratings = {}
    for product, ratings in product_ratings.items():
        product_avg_ratings[product] = sum(ratings) / len(ratings)
    
    best_rated_product = max(product_avg_ratings.items(), key=lambda x: x[1])
    print(f"Highest rated product: {best_rated_product[0]} ({best_rated_product[1]:.2f}/5)")

def create_summary_report(sales_data, filename):
    """Create a summary report and save to file"""
    if not sales_data:
        return
    
    total_sales = sum(sale['total'] for sale in sales_data)
    num_transactions = len(sales_data)
    avg_transaction = total_sales / num_transactions if num_transactions > 0 else 0
    
    # Product analysis
    product_stats = {}
    for sale in sales_data:
        product = sale['product']
        if product not in product_stats:
            product_stats[product] = {'revenue': 0, 'quantity': 0}
        product_stats[product]['revenue'] += sale['total']
        product_stats[product]['quantity'] += sale['quantity']
    
    top_product = max(product_stats.items(), key=lambda x: x[1]['revenue'])
    
    # Create report
    report = f"""
SALES SUMMARY REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERVIEW:
- Total Revenue: ${total_sales:,.2f}
- Total Transactions: {num_transactions}
- Average Transaction: ${avg_transaction:.2f}

TOP PRODUCT:
- {top_product[0]}: ${top_product[1]['revenue']:,.2f} revenue, {top_product[1]['quantity']} units sold

DETAILED BREAKDOWN:
"""
    
    for product, stats in sorted(product_stats.items(), key=lambda x: x[1]['revenue'], reverse=True):
        report += f"- {product}: ${stats['revenue']:,.2f} ({stats['quantity']} units)\n"
    
    with open(filename, 'w') as f:
        f.write(report)
    
    print(f"\nSummary report saved to {filename}")

def main():
    """Main function to run the data analysis example"""
    print("PYTHON DATA ANALYSIS EXAMPLE")
    print("="*50)
    
    # Generate or load sample data
    csv_filename = "sales_data.csv"
    sales_data = load_data_from_csv(csv_filename)
    
    if not sales_data:
        sales_data = generate_sample_data()
        save_data_to_csv(sales_data, csv_filename)
    else:
        print(f"Loaded {len(sales_data)} records from {csv_filename}")
    
    # Perform analysis
    analyze_sales_data(sales_data)
    
    # Create summary report
    create_summary_report(sales_data, "sales_report.txt")
    
    print("\n" + "="*50)
    print("Data analysis completed!")
    print("Files created:")
    print("- sales_data.csv (raw data)")
    print("- sales_report.txt (summary report)")
    print("="*50)

if __name__ == "__main__":
    main()