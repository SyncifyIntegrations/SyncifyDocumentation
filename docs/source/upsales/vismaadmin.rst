====================
Visma Administration
====================

Overview
=========

The integration between Upsales and Visma Administration is a solution designed to enhance business efficiency by automating the flow of data between Upsales and Visma Administration. 
This integration streamlines operations, reduces manual data entry, and ensures accuracy across sales and customer data management processes. 

Save time with automatic transfer of your orders/invoices to Visma Administration, and eliminate the double work of entering data into two systems. This process streamlines operations, enhancing efficiency by automating tasks that would otherwise require manual input across different platforms.

Printscreens
=============

:doc:`Default field mappings for the integration can be found here. <vismaadmin/vismaadmin-printscreens>`

How it works
-----------------

- Migrate data from Visma to ensure that Upsales has all the latest data from the ERP system. The migration includes all historic customers, contact persons, products, invoices/orders.
- All created or updated products in Visma are automatically synchronized to Upsales.
- Customers, contact persons and orders/invoices are automatically synchronized between the two systems. This means that if any update or new customer is added to either system, it is reflected in the other system.

Customize your integration
-----------------------------------

- The integration is customizable to precisely match your needs. Whether you're looking to add or exclude specific fields from the integration, necessary adjustments can be made with ease.
- Need to synchronize more than one company in Visma to Upsales? We got you covered!

Activating Visma Application
--------------------------------------------

In order to get the service up and running, we have to access your Visma-server and install our service. To start this process, please get in contact with your contact person, or Syncify at kundsupport@syncify.se.

App Settings
---------------

+----------------------+--------------------------------------------------------------------------------------------------+
|   **App Setting**    |                                        **Specification**                                         |
+======================+==================================================================================================+
| **Module to sync**   | Choose what should be synchronized from Visma to Upsales and to which                            |
|                      | module Upsales should sync with Visma.                                                           |
|                      |                                                                                                  |
| - **Invoice**        | Order/Sales opportunity sent from Upsales will directly turn into an invoice in                  |
|                      | Visma, invoice data will also be sent back to the same order/sales                               |
|                      | opportunity in Upsales.                                                                          |
|                      |                                                                                                  |
| - **Order**          | Order/Sales opportunity sent from Upsales will create an order in Visma,                         |
|                      | order data will also be sent back to the same order/sales opportunity in Upsales.                |
+----------------------+--------------------------------------------------------------------------------------------------+
| **Placeholder User** | Selected user will be listed as a reference on order or invoice, if no user is                   |
|                      | specified in 'Our Reference.'                                                                    |
+----------------------+--------------------------------------------------------------------------------------------------+
|                      |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+
| **Visma Settings**   | **These settings are only used to establish a connection with Visma.**                           |
+----------------------+--------------------------------------------------------------------------------------------------+
| Company Path         | The location of the company in the storage unit, including the company name.                     |
+----------------------+--------------------------------------------------------------------------------------------------+
| Username             | Username for the API-user.                                                                       |
+----------------------+--------------------------------------------------------------------------------------------------+
| Password             | Password for the API-user.                                                                       |
+----------------------+--------------------------------------------------------------------------------------------------+
|                      |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+
| **Sync Settings**    |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+
| Sync Products        | Sets whether or not products are synced from Visma to Upsales.                                   |
+----------------------+--------------------------------------------------------------------------------------------------+
| Sync Contacts        | Sets whether or not contacts are synced between Upsales and Visma.                               |
+----------------------+--------------------------------------------------------------------------------------------------+
|                      |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+



Detailed Service Description
========================

Initial migration
---------------------

All customers, products, invoices/orders from Visma are synced to Upsales.
(The initial date can be set to a specific date if desired).

Companies
-------------
    - Creating a company in Upsales? Syncing occurs only if the company's status in the journey is marked as 'Customer'. This can however be changed in the configuration.
    - Creating a company in Visma? Syncing with Upsales happens automatically.
    - Updates made on a company? As long as the journey status is 'Customer' (or whatever configured status), syncing will occur automatically from Upsales. Company updates from Visma always sync automatically.

Products
-------------
    - Products are only synced from Visma to Upsales. This happens automatically whenever a new product is created or updated in Visma.

Invoices
--------------
    - Invoices created in Visma are automatically synced to Upsales as long as they are not marked as 'Not done'.
    - Customer number is mandatory.

Orders
--------------
    - Orders are automatically created in Visma when a sale/opportunity reaches the configured order stage in Upsales.
    - Orders created in Visma will automatically be sent to Upsales as long as they are not marked as 'Not done'.
    - Customer number is mandatory.

.. important::

   The integration does **NOT** 
   sync deletions between the systems. For instance, if a customer is deleted in Upsales, it is **NOT** deleted in Visma, the same goes for the other way around, and all synced objects.