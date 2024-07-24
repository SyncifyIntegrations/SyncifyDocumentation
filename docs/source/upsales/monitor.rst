============
Monitor  G5
============

Overview
=========

The integration between Upsales and Monitor G5 is a strategic solution designed to enhance business efficiency by automating the flow of data between Upsales and Monitor G5. 
This integration streamlines operations, reduces manual data entry, and ensures accuracy across sales and customer data management processes. 

Save time with automatic transfer of your orders/invoices to Monitor, and eliminate the double work of entering data into two systems. This process streamlines operations, enhancing efficiency by automating tasks that would otherwise require manual input across different platforms.

Printscreens
=============

:doc:`Default field mappings for the integration can be found here. <monitor/monitor-printscreens>`

How it works
-----------------

- Migrate data from Monitor to ensure that Upsales has all the latest data from the ERP system. The migration includes all historic customers, contact persons, products, invoices/orders (depending on chosen module).
- All created or updated products in Monitor are automatically synchronized to Upsales.
- Customers, contact persons and orders/invoices are automatically synchronized between the two systems. This means that if any update or new customer is added to either system, it is reflected in the other system.
- The integration provides additional “good to have” features such as: timestamps indicating the last or first synchronization of objects, and notifications for the synchronization of invoices and orders.

Customize your integration
-----------------------------------

- The integration is customizable to precisely match your needs. Whether you're looking to add or exclude specific fields from the integration, necessary adjustments can be made with ease.
- Need to synchronize more than one company in Monitor to Upsales? We got you covered!

Activating Monitor Application
--------------------------------------------

In order to get the service up and running, we have to access your Monitor-server and install our service. To start this process, please get in contact with your contact person, or Syncify at kundsupport@syncify.se.

App Settings
---------------

+----------------------+--------------------------------------------------------------------------------------------------+
|   **App Setting**    |                                        **Specification**                                         |
+======================+==================================================================================================+
| **Module to sync**   | Choose what should be synchronized from Monitor to Upsales and to which                          |
|                      | module Upsales should sync with Monitor.                                                         |
|                      |                                                                                                  |
| - **Invoice**        | Order/Sales opportunity sent from Upsales will directly turn into an invoice in                  |
|                      | Monitor, invoice data will also be sent back to the same order/sales                             |
|                      | opportunity in Upsales.                                                                          |
|                      |                                                                                                  |
| - **Order**          | Order/Sales opportunity sent from Upsales will create an order in Monitor,                       |
|                      | order data will also be sent back to the same order/sales opportunity in Upsales.                |
+----------------------+--------------------------------------------------------------------------------------------------+
| **Placeholder User** | Selected user will be listed as a reference on order or invoice, if no user is                   |
|                      | specified in 'Our Reference.'                                                                    |
+----------------------+--------------------------------------------------------------------------------------------------+
|                      |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+
| **Monitor Settings** | **These settings are only used to establish a connection with Monitor.**                         |
+----------------------+--------------------------------------------------------------------------------------------------+
| API-Url to Monitor   | API-Url of the company in Monitor which the integration should establish a connection to Monitor |
+----------------------+--------------------------------------------------------------------------------------------------+
| Username             | Username for the API-user.                                                                       |
+----------------------+--------------------------------------------------------------------------------------------------+
| Password             | Password for the API-user.                                                                       |
+----------------------+--------------------------------------------------------------------------------------------------+
|                      |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+
| **Sync Settings**    |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+
| Sync Products        | Sets whether or not products are synced from Monitor to Upsales.                                 |
+----------------------+--------------------------------------------------------------------------------------------------+
| Sync Contacts        | Sets whether or not contacts are synced between Upsales and Monitor.                             |
+----------------------+--------------------------------------------------------------------------------------------------+
|                      |                                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------+

.. warning::
    The underlying settings may incur an additional cost, please get in touch with your contact
    person before enabling them.

+------------------------------+-------------------------------------------------------------------------------------+
|   Customer Customizations    |           These settings will add additional fields to the customer sync.           |
|                              |                                                                                     |
+==============================+=====================================================================================+
| Sync Currency                | Syncs the customers currency.                                                       |
+------------------------------+-------------------------------------------------------------------------------------+
| Sync Customer Number Invoice | Syncs the customer number invoice field.                                            |
+------------------------------+-------------------------------------------------------------------------------------+
| Sync Communication Address   | Syncs the field Communication Address on the Customer card, with type Invoice.      |
| Invoice                      |                                                                                     |
+------------------------------+-------------------------------------------------------------------------------------+
| Sync Communication Address   | Syncs the field Communication Address on the Customer card, with type Order.        |
| Order                        |                                                                                     |
+------------------------------+-------------------------------------------------------------------------------------+
| **DON'T** sync blocked       | Makes sure that blocked customers are ignored when syncing from Monitor to Upsales. |
| customers                    |                                                                                     |
+------------------------------+-------------------------------------------------------------------------------------+
| Sync payment terms           | Syncs payment terms.                                                                |
+------------------------------+-------------------------------------------------------------------------------------+


+-----------------------------+--------------------------------------------------------------+
|    Order Customizations     | These settings will add additional fields to the order sync. |
|                             |                                                              |
+=============================+==============================================================+
| Sync Customers Order Number | Syncs the field Customers Order Number.                      |
+-----------------------------+--------------------------------------------------------------+
| Sync Order Status           | Syncs the order status of the order.                         |
+-----------------------------+--------------------------------------------------------------+
| Sync Invoice Address        | Syncs the invoice address of the order.                      |
+-----------------------------+--------------------------------------------------------------+


+------------------------+------------------------------------------------------------------------------------+
| Product Customizations |           These settings will add additional fields to the product sync.           |
|                        |                                                                                    |
+========================+====================================================================================+
| Sync Extra Description | Syncs the field Extra Description.                                                 |
+------------------------+------------------------------------------------------------------------------------+
| Product filter         | This setting makes it so that only products with a certain category in Monitor are |
|                        | synced to Upsales.                                                                 |
+------------------------+------------------------------------------------------------------------------------+
| Sync Price List Value  | Price is taken from the given price list instead of the field 'Standard Price'.    |
+------------------------+------------------------------------------------------------------------------------+



.. note::
    To sync multiple Monitor companies to Upsales, please get in touch with your contact
    person.

Detailed Service Description
==============================

Initial migration
---------------------

All customers, products, invoices/orders from Monitor are synced to Upsales.
(The initial date can be set to a specific date if desired).

Companies
-------------
    - Creating a company in Upsales? Syncing occurs only if the company's status in the journey is marked as 'Customer'. This can however be changed in the configuration.
    - Creating a company in Monitor? Syncing with Upsales happens automatically.
    - Updates made on a company? As long as the journey status is 'Customer' (or whatever configured status), syncing will occur automatically from Upsales. Company updates from Monitor always sync automatically.

Products
-------------
    - Products are only synced from Monitor to Upsales. This happens automatically whenever a new product is created or updated in Monitor.

Invoices
--------------
    - Invoices created in Monitor are automatically synced to Upsales.

Orders
--------------
    - Orders are automatically created in Monitor when a sale/opportunity reaches the configured order stage in Upsales.

.. important::

   The integration does **NOT** 
   sync deletions between the systems. For instance, if a customer is deleted in Upsales, it is **NOT** deleted in Monitor, the same goes for the other way around, and all synced objects.