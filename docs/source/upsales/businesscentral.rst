=================
Business Central
=================

Overview
=========

This integration is designed to streamline your business processes by enabling seamless data transfer between Business Central, a leading enterprise resource planning system, and Upsales, a robust customer relationship management system. 
By leveraging the strengths of both systems, businesses can enhance their operational efficiency, improve data accuracy, and offer superior customer experiences.

Save time with automatic transfer of your orders/invoices to Business Central, and eliminate the double work of entering data into two systems. This process streamlines operations, enhancing efficiency by automating tasks that would otherwise require manual input across different platforms.

Printscreens
=============

:doc:`Default field mappings for the integration can be found here. <businesscentral/businesscentral-printscreens>`

How it works
------------------

- Migrate data from Business Central to ensure that Upsales has all the latest data from the ERP system. The migration includes all historic customers, contact persons, products, invoices/orders (depending on chosen module).
- All created or updated products in Business Central are automatically synchronized to Upsales.
- Customers, contact persons and orders/invoices are automatically synchronized between the two systems. This means that if any update or new customer is added to either system, it is reflected in the other system.
- The integration provides additional “good to have” features such as: timestamps indicating the last or first synchronization of objects, and notifications for the synchronization of invoices and orders.

Customize your integration
-----------------------------------

- The integration is customizable to precisely match your needs. Whether you're looking to add or exclude specific fields from the integration, necessary adjustments can be made with ease.
- Need to synchronize more than one company in Business Central to Upsales? We got you covered!

Boarding Guide
==================

The boarding process is designed to be efficient and straightforward, ensuring a smooth and hassle-free experience.

:doc:`Click here to read a step by step tutorial of the boarding process. <businesscentral/businesscentral-boarding>`

Application Settings
==========================================

+---------------------------------+--------------------------------------------------------------------------------------+
| **App Setting**                 | **Specification**                                                                    |
+=================================+======================================================================================+
| **Module to sync**              | Choose what should be synchronized from Business Central to Upsales and to which     |
|                                 | module Upsales should sync with Business Central.                                    |
|                                 |                                                                                      |
| - **Invoice**                   | Order/Sales opportunity sent from Upsales will directly turn into an invoice in      |
|                                 | Business Central, invoice data will also be sent back to the same order/sales        |
|                                 | opportunity in Upsales.                                                              |
|                                 |                                                                                      |
| - **Order**                     | Order/Sales opportunity sent from Upsales will create an order in Business Central,  |
|                                 | order data will also be sent back to the same order/sales opportunity in Upsales.    |
+---------------------------------+--------------------------------------------------------------------------------------+
| **Placeholder User**            | Selected user will be listed as a reference on order or invoice, if no user is       |
|                                 | specified in 'Our Reference.'                                                        |
+---------------------------------+--------------------------------------------------------------------------------------+
| **Won Order Stage**             | The stage on the sales board when an invoice or order should be sent to Business     |
|                                 | Central.                                                                             |
+---------------------------------+--------------------------------------------------------------------------------------+
| **Lost Order Stage**            | The stage on the Upsales sales board that corresponds to a canceled/credited         |
|                                 | order/invoice coming from Business Central.                                          |
+---------------------------------+--------------------------------------------------------------------------------------+
| **Connect to Business Central** | This is the final part of the boarding, here an user with permissions to the         |             
|                                 | API/Webservices needs to log in using the “Sign in with Microsoft” button. There the |
|                                 | user will be prompted to authorize the integration. After authorization a new page   |
|                                 | will appear where the user will have to choose the company in Business Central they  |
|                                 | wish to connect to Upsales. Provided that all previous steps in the boarding process |
|                                 | are done correctly, the user will be redirected back to Upsales. The message         |
|                                 | “Connected with oAuth” should appear. Click “Save” when all settings are set up, and |
|                                 | you’re done.                                                                         |
|                                 |                                                                                      |
+---------------------------------+--------------------------------------------------------------------------------------+

.. note::
    To sync multiple Business Central companies to Upsales, please get in touch with your contact
    person.

Detailed Service Description
=======================

Initial migration
---------------------

All customers, products, invoices/orders from Business Central are synced to Upsales.
(The initial date can be set to a specific date if desired).

Companies
-------------
    - Creating a company in Upsales? Syncing occurs only if the company's status in the journey is not marked as 'Lead'.
    - Creating a company in Business Central? Syncing with Upsales happens automatically.
    - Updates made on a company? As long as the journey status is not “Lead”, syncing will occur automatically. Companies from Business Central always sync automatically.

Products
-------------
    - Products are only synced from Business Central to Upsales.

Invoices
--------------
    - You can choose to sync sales in Upsales to orders or invoices in Business Central.
    - Choose invoice, and an invoice is automatically created in Business Central when a sale/opportunity has 100% probability.
    - Invoices created in Business Central are automatically synced to Upsales as well.

Orders
--------------
    - Choose order, and an order is automatically created in Business Central when a sale/opportunity has 100% probability.
    - Orders created in Business Central are automatically synced to Upsales as well.

.. important::

   The integration does **NOT** 
   sync deletions between the systems. For instance, if a customer is deleted in Upsales, it is **NOT** deleted in Monitor, the same goes for the other way around, and all syncs.