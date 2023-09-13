# 1.0 Introduction
## 1.1 Purpose 
The purpose of this document is to give a detailed description of My Library System. It will explain the features, the interfaces, what the system will do, and the constraints under which it must operate. This document is created for both stakeholder and the developer of the system. 

## 1.2 Scope of Project
This software system will be a Library Management System for a small library in my imaginary town of Moyudan. This system will be designed to streamline library operations, improving user experiences, and ensuring efficient resource management. It helps the library provide better services to their users while maintaining integrity of their collections.

More specifically, this system will be able to do the following:
1. Cataloging and Organization: This system will help the library efficiently catalog and organize their collections. It allows librarians to create detailed records for each item in the library, including books, journals, multimedia materials, and more. This cataloging process includes information such as titles, authors, publishers, publication dates, ISBNs, and more.
2. Inventory Management: This system will enable librarians to keep track of the library's inventory. It helps in monitoring the availability of items, managing check-outs and returns, and identifying lost or missing materials. This helps maintain the integrity of the library's collection.
3. User Management: This system will allow librarians to manage user accounts, including registration, authentication, and user data. It tracks the borrowing history of patrons, helping librarians to serve their needs better.
4. Circulation Control: This system will automate the circulation process, making it easier for library users to check out and return items. It also manages due dates and fines for overdue materials.
5. Search and Discovery: This system will make it easy for users to find materials in the library's collection. Users can search by title, author, subject, keyword, or other criteria.
6. Reservations and Holds: This system will allow users to reserve or place holds on items that are currently checked out. It will manage these requests and notifies users when the items become available.
7. Reporting and Analytics: This system will enable librarians to generate reports and analyze library data. This information helps in making informed decisions about collection development, resource allocation, and user services.
8.  Security and Privacy: This system will help maintaining the security of user data and library resources. It may include features like user authentication, role-based access control, and data encryption.

## 1.3 Glossary
|Term|Definition|
|----|----------|
|Library User|An individual who interacts with the library system to borrow, return, search for materials, and manage their account.|
|Librarian|Library staff members responsible for managing the library's operations, including user accounts, materials, and events.|
|User Account| A personal account created by library users, containing information such as contact details, borrowing history, and current loans.|
|Materials|Library materials, including books, journals, magazines, and digital resources.|
|Catalog|A database or repository that stores information about library materials.|
|Cataloging|The process of adding new library materials to the library's catalog, including data entry, categorization, and generating unique identifiers.|
|Due Date|The date by which a borrowed library item must be returned to the library to avoid late fees or fines.|
|Reservation|A request made by a library user to reserve a library item that is currently checked out by another user. The user is notified when the item becomes available.|
|Renewal|The process by which a library user extends the due date of a borrowed item, typically if there are no holds or reservations on the item.|
|Overdue Items|Library materials that have not been returned by the due date, often subject to late fees or fines.|

## 1.4 Reference
https://www.ala.org/advocacy/privacy/guidelines/library-management-systems

## 1.5 Overview of Document
The next chapter, the Overall Description section, of this document gives an overview of the functionality of the product. It describes the informal requirements and its is used to establish context fot the technical requirements specification in the next chapter.

The third chapter, Requirements Specification sectin, of this document is written primarily for the developer and describes in technical terms the details of the functionality of the product.

Both sections of the document desribe the same software product in its entirety, but are intended for different audience and thus use different language.

# 2.0 Overall Description
## 2.1 System Environment
The Library System has two active actors and one cooperating system. 

Users can access the online functions through the internet to check the availability of a certain material and/or reserve it. Users can also extend their lending through the online functions. To borrow or return materials, users has to access the system directly from the library. 

Librarians access the system directly from the library to catalog new materials, manage users account, and generate reports.

## 2.2 Use Cases
This section outlines the use cases for each of the active actors separately. The reader, the author and the reviewer have only one use case apiece while the editor is main actor in this system.

### 2.2.1 Librarian Use Case
1. Administering User Accounts:  
Description: Libarians can manage user accounts, including creating, suspending, or deactivating accounts, and resetting passwords.

2. Cataloging New Materials:  
Description: Librarians add new materials to the library's catalog, including books, journals, and digital resources. The system generates unique identifiers and updates the catalog.

3. Inventory Management:  
Description: Librarians can perform physical inventory checks, update item locations, and mark items as lost or damaged. The system keeps track of inventory changes.

4. Generating Reports:  
Description: Librarians can generate reports on circulation statistics, inventory status, overdue items, and other library-related data.

### 2.2.2 Library User Use Case
1. User Registration:  
Description: A library user creates a new account by providing personal information and email address. The system verifies the information and issues a unique library ID.

2. Browsing and Searching for Materials:  
Description: Users search for books, journals, or other materials using various search criteria such as title, author, subject, or keyword. The system displays search results and allows users to browse through available items.

3. Borrowing Materials:  
Description: A user selects a specific item from the catalog, scans their library card, and checks out the material. The system records the due date for return and updates the item's status.

4. Returning Materials:  
Description: Users return borrowed materials by scanning their library card and the item's barcode. The system updates the item's status and calculates any late fees, if applicable.

5. Placing Holds/Reservations:  
Description: A user can place a hold or reserve an item that is currently checked out by another user. The system notifies the user when the item becomes available.

6. Renewing Materials:  
Description: Users can request to renew materials that they have checked out if there are no holds or reservations on those items. The system extends the due date if renewal is possible.

7. Managing User Account:  
Description: Users can view their borrowing history, fines, and update their contact information through their user account.

## 2.3 Non-Functional Requirements Specification
The Library Management system software and database will be on a server with high speed internet capability. 

In total, three client machines are needed in the library. One for the librarians in the staff desk, and two for users to borrow and return materials. The actual machine specifications will be explained in section ...

User authentication is required to use any of the system function, except for basic search function, which anybody can access. The server on which the system resides will have its own security to prevent unauthorized write/delete access.

# 3.0 Requirements Specification 
## 3.1 Functional Requirements
### 3.1.1 Administer User Accounts
**ID:** FR-001  
**Title:** Administer User Accounts  
**Description:** The Library System shall provide administrative functionality to manage user accounts. Authorized librarians shall have the ability to perform the following actions on user accounts:  

**Administer User Accounts Actions:** 
**1. Create User Accounts**
* Authorized librarians be able to create new user accounts by entering the user's:
   * Full name
   * Username (unique)
   * Email address (unique)
   * Password
   * User role (e.g., librarian, user)
* The system shall generate unique user ID for each created account.

**2. Modify User Accounts**  
* Authorized librarians have the ability to modify existing user account details, including:
  * Full name
  * Email address
  * Passord
  * User role
* Changes made by librarians shall be saved and reflected in the user account information.

**3. Deactivate User Accounts**  
* Authorized librarians shall be able to deactivate user accounts, preventing users from accessing the system while retaining their account data.
* Deactivated users shall not be able to log in or use system resources until their account is reactivated.  

**4. Reactivate User Accounts**  
* Authorized librarians shall have the capability to reactivate previously deactivated user accounts, restoring their access to the system.  

**5. Delete User Accounts**  
* Authorized librarians  shall have the authority to permanently delete user accounts from the system, including all associated data.
* A confirmation prompt shall appear before deletion to prevent accidental removal.

**6. Search User Accounts**  
* Authorized librarians shall be able to search for user accounts based on criteria such as username, email address, or user role.
* The system shall display a list of matching user accounts that meet the search criteria.

### 3.1.2 Cataloging New Materials
**ID:** FR-002  
**Title:** Cataloging New Materials   
**Description:** The system shall provide functionality for librarian to catalog new materials, including books, periodicals, and other library resources. This cataloging process involves entering and maintaining essential information about each item in the library's collection.

**Cataloging New Materials Actions:**  
**1. Add New Material:**
* Library staff shall be able to add new materials to the library's collection.
* For each new material, the following information shall be captured:
  * Title (mandatory)
  * Author(s)
  * ISBN (International Standard Book Number) or ISSN (International Standard Serial Number) for periodicals
  * Publication date
  * Genre or category (e.g., fiction, non-fiction, reference)
  * Physical location in the library (e.g., shelf number)
  * Quantity of copies available
  * Description or summary
  * Cover image (optional)

**2. Edit Material Information:** 
* Library staff shall have the ability to edit and update the information associated with existing materials.
* Any changes made to material details shall be reflected in the catalog.

**3. Delete Material Records:**
* Library staff with appropriate privileges shall be able to permanently remove material records from the catalog.
* A confirmation prompt shall appear before deleting to prevent accidental removal.

**4. Search and Retrieve Material Information:**
* The system shall provide a search functionality that allows library staff to find materials based on various criteria, including title, author, ISBN/ISSN, genre, and publication date.
* Search results shall display relevant material details.

**5. Check for Duplicate Entries:**
* When adding new materials, the system shall perform checks to identify potential duplicate entries to avoid redundancy.

**Validation and Error Handling:**
**1. Data Validation:** 
* The system shall validate data entered during the cataloging process to ensure accuracy and completeness.
* Users shall be alerted to any missing or incorrect information.

**2. Error Handling:**
* The system shall provide clear error messages and guidance if any cataloging errors occur.
* It shall allow users to correct errors and resubmit information.
Access Control:

**Access Control:**  
**1. Access Control:**
* Only authorized library staff members with appropriate privileges shall have access to the cataloging functionality.
* Access control measures shall be in place to protect the integrity of the catalog data.

### 3.1.3 Inventory Management
**ID:** FR-003  
**Title:** Inventory Management  
**Description:** The system shall provide comprehensive inventory management functionality to enable library staff to efficiently manage the library's collection of materials. This includes tracking, updating, and organizing the library's inventory of books, periodicals, and other resources.

**Inventory Management Actions:**  
**1. Track Material Status:**  
* The system shall maintain the status of each material in the library's collection, indicating whether it is available for borrowing, checked out, on hold, in transit, or missing.
* The status shall be automatically updated when materials are borrowed, returned, or transferred between library branches.

**2. Check In/Out Materials:**  
* Library staff shall have the ability to check materials in and out on behalf of library patrons.
* Patrons shall also be able to self-check materials in and out using a self-service kiosk or online portal.

**3. Reserve and Hold Materials:**  
* Library patrons shall be able to place holds or reservations on materials that are currently checked out.
* The system shall notify patrons when the reserved materials become available for pick-up.

**4. Renew Materials:**  
* Patrons shall have the option to renew materials they have borrowed, provided that the materials are not on hold for another patron.
* Renewal requests shall be subject to renewal limits and overdue fines, if applicable.

**5. Calculate Late Fees:**  
* The system shall calculate and apply late fees or fines for overdue materials based on defined library policies.
* Patrons shall be notified of accrued fines and be provided with a mechanism to pay them.

**Inventory Tracking:**  
**1. Inventory Updates:**  
* The system shall automatically update the inventory count when materials are added, checked out, returned, or removed from the collection.
* Manual adjustments shall also be possible for correcting discrepancies.

**2. Material Location Tracking:**  
* The system shall keep track of the physical location of each material within the library, including shelf numbers and sections.

**Reservation and Requests:**  
**1. Handling Reservations and Requests:**  
* The system shall manage reservations and requests for materials efficiently, ensuring fair allocation when multiple patrons request the same item.
* Priority for reservations shall be based on a predefined order, such as first come, first served.

**Notifications and Alerts:**  
**1. Notifications:**  
* The system shall send notifications and alerts to library staff and patrons for various events, such as due date reminders, hold availability, and overdue notices.

**Access Control:**  
**1. Access Control**
* Only authorized library staff members shall have access to perform inventory management actions.
* Access control measures shall be in place to protect the integrity of the inventory data.

### 3.1.4 Generating Reports
**ID:** FR-004   
**Title:** Generating Reports   
**Description:** The system shall provide functionality to generate a variety of reports to help library staff and administrators monitor and analyze library operations and collections effectively.  
**Actions**  
**Access Control**     

### 3.1.4 Placing Reservations  
**ID:** FR-005   
**Title:** Placing Reservations  
**Description:** The system shall provide functionality for library patrons to place holds or reservations on library materials that are currently checked out or unavailable. This feature enables patrons to reserve materials for future borrowing.  
**Actions:**  
**1. Predefined Reports:**  
* The system shall offer a set of predefined reports commonly needed for library management, including but not limited to:  
  1. Inventory Summary Report: A summary of the library's entire collection, categorized by type, status, and location.  
  2. Patron Activity Report: A report detailing patron borrowing and return activities.
  3. Overdue Materials Report: A list of materials that are currently overdue, including patron details.
  4. Usage Statistics Report: Statistical data on the library's most borrowed materials, popular genres, and patron demographics.  

**2. Custom Report Creation:**  
* Library staff and administrators shall have the ability to create custom reports by selecting specific data fields and criteria to include.
* Custom reports shall be savable and reusable for future reference.

**3. Report Scheduling:**  
* The system shall allow scheduled generation of reports, such as weekly or monthly, and the automatic delivery of these reports to designated recipients via email.

**4. Export and Printing:**  
* Generated reports shall be exportable in common formats (e.g., PDF, Excel) and printable for physical records and sharing with stakeholders.

**Report Parameters and Filters:**   
**1. Report Parameters:**  
* The system shall prompt users to input necessary parameters when generating custom reports, including date ranges, material types, and other relevant filters.  


### 3.1.4 Functional Requirements  
**ID:**   
**Title:**   
**Description:**   
**Actions**  
**Access Control**     



### Access Control:
Access to report generation and customization shall be controlled by user roles and permissions, ensuring that only authorized staff and administrators can create and view reports.

## 3.2 Non-Functional Requirements