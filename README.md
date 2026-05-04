# Module 8: GlobalTech Solutions Customer Management System
This repository contains a backend logic prototype for a Customer Relationship Management (CRM) and Project Tracking system. The project focuses on using Python dictionaries to store, retrieve, and analyze multi-layered business data, including client profiles, service rates, and project financials.

## Files Included
- `module08-assignment.py`: The main Python script featuring nested dictionary structures, data aggregation logic, and customer validation functions

## What I Practiced
In this assignment, I moved beyond simple variables to manage complex relational data structures:
- **Nested Dictionary Architecture**: Designed a system where unique Customer IDs act as keys to access detailed sub-dictionaries containing contact information and project lists
- **Data Lookup & Safe Retrieval**: Implemented secure data access using the `.get()` method to handle missing keys without crashing the program
- **Automated Financial Calculations**: 
  - Developed logic to cross-reference project hours against service rate dictionaries to calculate real-time project costs
  - Created a financial summary report tracking total hours, budget averages, and maximum/minimum project spends
- **Data Transformation & Logic**:
  - **Dictionary Comprehensions**: Used advanced Python syntax to create 10% rate increases and categorize services into "Premium," "Standard," or "Basic" tiers based on price.
  - **Filtering**: Generated a live list of "Active Customers" by filtering for profiles with at least one associated project
- **Validation & Recommendation Engines**:
  - Built a validation function to ensure all required contact fields are present in a customer profile
  - Developed a recommendation engine that suggests new services to clients based on their project history and budget constraints

## Key Business Insights
- **Service Usage Analysis**: Generated a summary of which services (e.g., Cloud Computing, Data Analysis) are most frequently requested
- **Project Status Tracking**: Provided a high-level view of how many projects are currently "Active," "Pending," or "Completed"
- **Detailed Budgeting**: Analyzed total and average budgets on a per-customer basis to identify high-value clients
