# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# 1
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Computing": 200,
    "Cybersecurity": 225,
    "IT Support": 90
}

# 2
customer1 = {
    "company_name": "TechFlow Inc", 
    "contact_person": "Alice Johnson", 
    "email": "alice@techflow.com", 
    "phone": "000-0001"
}
customer2 = {
    "company_name": "Green Energy Co", 
    "contact_person": "Bob Smith", 
    "email": "bob@greenenergy.org", 
    "phone": "000-0002"
}
customer3 = {
    "company_name": "Global Logistics", 
    "contact_person": "Charlie Davis", 
    "email": "charlie@globallog.com", 
    "phone": "000-0003"
}
customer4 = {
    "company_name": "Urban Retail", 
    "contact_person": "Diana Prince", 
    "email": "diana@urbanretail.com", 
    "phone": "000-0004"
}

# 3
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# 4
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(f"ID: {cid} | Company: {info['company_name']} | Contact: {info['contact_person']}")

# 5
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\nCustomer Lookups:")
print("-" * 60)
print(f"C002 Info: {c002_info}")
print(f"C003 Contact: {c003_contact}")
print(f"C999 Search: {c999_info}")

# 6
customers["C001"]["phone"] = "000-0001"
customers["C002"]["industry"] = "Renewable Energy"

print("\nUpdating Customer Information:")
print("-" * 60)
print(f"Updated C001 Phone: {customers['C001']['phone']}")
print(f"Added C002 Industry: {customers['C002']['industry']}")

# 7
projects = {
    "C001": [
        {"name": "E-commerce Portal", "service": "Web Development", "hours": 120, "budget": 20000, "status": "completed"},
        {"name": "Data Migration", "service": "Data Analysis", "hours": 40, "budget": 8000, "status": "active"}
    ],
    "C002": [
        {"name": "Cloud Infrastructure", "service": "Cloud Computing", "hours": 80, "budget": 18000, "status": "active"}
    ],
    "C003": [
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 50, "budget": 12000, "status": "pending"}
    ],
    "C004": [
        {"name": "Data Migration", "service": "Data Analysis", "hours": 40, "budget": 8000, "status": "active"}
        ] 
}

print("\nProject Information:")
print("-" * 60)
for cid, proj_list in projects.items():
    print(f"Customer {cid} has {len(proj_list)} project(s).")

# 8
print("\nProject Cost Calculations:")
print("-" * 60)
for cid, proj_list in projects.items():
    for p in proj_list:
        rate = services.get(p["service"], 0)
        cost = rate * p["hours"]
        print(f"Project: {p['name']} | Calculated Cost: ${cost}")

# 9
all_ids = list(customers.keys())
company_names = [c["company_name"] for c in customers.values()]
total_cust_count = len(customers)

print("\nCustomer Statistics:")
print("-" * 60)
print(f"Customer IDs: {all_ids}")
print(f"Total Customers: {total_cust_count}")

# 10
service_counts = {}
for proj_list in projects.values():
    for p in proj_list:
        s_type = p["service"]
        service_counts[s_type] = service_counts.get(s_type, 0) + 1

print("\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# 11
all_project_data = [p for sublist in projects.values() for p in sublist]
total_hours = sum(p["hours"] for p in all_project_data)
total_budget = sum(p["budget"] for p in all_project_data)
avg_budget = total_budget / len(all_project_data) if all_project_data else 0
max_budget = max(p["budget"] for p in all_project_data)
min_budget = min(p["budget"] for p in all_project_data)

print("\nFinancial Summary:")
print("-" * 60)
print(f"Total Hours: {total_hours} | Total Budget: ${total_budget}")
print(f"Avg Budget: ${avg_budget:.2f} | Max: ${max_budget} | Min: ${min_budget}")

# 12
print("\nCustomer Summary Report:")
print("-" * 60)
for cid, info in customers.items():
    cust_projects = projects.get(cid, [])
    p_count = len(cust_projects)
    p_hours = sum(p["hours"] for p in cust_projects)
    p_budget = sum(p["budget"] for p in cust_projects)
    print(f"Customer: {info['company_name']} ({cid})")
    print(f" - Projects: {p_count} | Hours: {p_hours} | Total Budget: ${p_budget}")

# 13
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate:.2f}")

# 14
active_customers = {cid: customers[cid] for cid, proj_list in projects.items() if len(proj_list) > 0}
print("\nActive Customers (with projects):")
print("-" * 60)
print(list(active_customers.keys()))

# 15
customer_budgets = {cid: sum(p["budget"] for p in proj_list) for cid, proj_list in projects.items()}
print("\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# 16
service_tiers = {
    s: ("Premium" if r >= 200 else "Standard" if r >= 100 else "Basic") 
    for s, r in services.items()
}
print("\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# 17
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    for field in required:
        if field not in customer_dict or not customer_dict[field]:
            return False
    return True

print("\nCustomer Validation:")
print("-" * 60)
for cid, info in customers.items():
    print(f"Customer {cid} valid: {validate_customer(info)}")

# 18
status_counts = {}
for proj_list in projects.values():
    for p in proj_list:
        status = p.get("status", "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1

print("\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# 19
def analyze_customer_budgets(projects_dict):
    stats = {}
    for cid, proj_list in projects_dict.items():
        if not proj_list:
            stats[cid] = {'total': 0, 'average': 0, 'count': 0}
            continue
        total = sum(p['budget'] for p in proj_list)
        stats[cid] = {
            'total': total,
            'average': total / len(proj_list),
            'count': len(proj_list)
        }
    return stats

detailed_stats = analyze_customer_budgets(projects)
print("\nDetailed Budget Analysis:")
print("-" * 60)
for cid, stat in detailed_stats.items():
    print(f"{cid}: {stat}")

# 20
def recommend_services(customer_id, customers, projects, services):
    cust_projects = projects.get(customer_id, [])
    used_services = [p['service'] for p in cust_projects]

    recommendations = [
        service for service, rate in services.items() 
        if service not in used_services and rate <= 175
    ]
    
    return recommendations

print("\nService Recommendations (Updated):")
print("-" * 60)
rec = recommend_services("C001", customers, projects, services)
print(f"Recommendations for C001: {rec}")
