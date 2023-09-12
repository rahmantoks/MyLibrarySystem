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

## 2.2 Functional Requirements Specification
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
**Description:** The Library System shall provide administrative functionality to manage user accounts. Authorized administrators shall have the ability to perform the following actions on user accounts:  

**Administer User Accounts Actions:** 

**1. Create User Accounts**
* Librarian shall be able to create new user accounts by entering the user's:
   * Full name
   * Username (unique)
   * Email address (unique)
   * Password
   * User role (e.g., librarian, user)
* The system shall generate unique user ID for each created account.

**2. Modify User Accounts**  
* Librarians shall have the ability to modify existing user account details, including:
  * Full name
  * Email address
  * Passord
  * User role
* Changes made by librarians shall be saved and reflected in the user account information.

**3. Deactivate User Accounts**  
* Administrators shall be able to deactivate user accounts, preventing users from accessing the system while retaining their account data.
* Deactivated users shall not be able to log in or use system resources until their account is reactivated.  

**4. Reactivate User Accounts**  
* Administrators shall have the capability to reactivate previously deactivated user accounts, restoring their access to the system.  

**5. Delete User Accounts**  
* Administrators shall have the authority to permanently delete user accounts from the system, including all associated data.
* A confirmation prompt shall appear before deletion to prevent accidental removal.

**6. Search User Accounts**  
* Administrators shall be able to search for user accounts based on criteria such as username, email address, or user role.
* The system shall display a list of matching user accounts that meet the search criteria.



## 3.2 Non-Functional Requirements