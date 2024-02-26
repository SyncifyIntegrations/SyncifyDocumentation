Boarding Guide
==================

This page is designed to offer comprehensive guidance on integrating Business Central with Upsales.

.. note::
    Please contact Syncify at kundsupport@syncify.se if further assistance is required.

    Note that this guide is intended for connecting Upsales with just **ONE** company in Business Central. If you are looking to connect more than one company, please contact us using the e-mail above.

.. warning::
    Our application employs user impersonation for establishing a connection with Business Central. As a result, our integration inherits the permissions of the user initiating the connection. 
    Consequently, it's critical that this user possesses the necessary permissions for **read and write** access to the API. 
    Additionally, the user must have the authority to approve **'Azure Applications'** for your organization.

**1.** Please log in to your Upsales CRM account and click on your profile located in the upper right corner of the screen.

**2.** To proceed, click on the "Apps" tab located in the navigation menu of your Upsales CRM account. This will allow you to access and manage the various applications and integrations available for use within the platform.

.. image:: /_static/printscreens/bc/boarding/BC-Boarding1.png

**3.** Please search for **Business Central by Syncify** and click on it to proceed.

.. image:: /_static/printscreens/bc/boarding/BC-Boarding2.png

**4.** Look for the **Buy** button, and click on it to initiate the activation process. This may involve providing some additional information or permissions, depending on the specific requirements of the integration.

.. image:: /_static/printscreens/bc/boarding/BC-Boarding3.png

**5.** Accept the terms and conditions.

**6.** Now head to Business Central and search for **Web Services** (may vary depending on language), then click on it to proceed.

.. image:: /_static/printscreens/bc/boarding/BC-Boarding4.png

**7.** Click on **Edit List** once you have accessed the **Web Services** page in Microsoft Business Central.

.. image:: /_static/printscreens/bc/boarding/BC-Boarding5.png

**8.** Make sure the following web service pages are active: 

+-----------+--------------------------+
| Object ID |       Service Name       |
+===========+==========================+
| 5050      | Contact                  |
+-----------+--------------------------+
| 21        | Customer                 |
+-----------+--------------------------+
| 14        | SalesPeople              |
+-----------+--------------------------+
| 6402      | SalesDocuments           |
+-----------+--------------------------+
| 6403      | SalesDocumentLines       |
+-----------+--------------------------+
| 312       | GenBusinessPostingGroups |
+-----------+--------------------------+
| 110       | CustomerPostingGroups    |
+-----------+--------------------------+
| 470       | VATBusinessPostingGroups |
+-----------+--------------------------+

If any web service is missing, please go ahead and click **New**. The object type should be **Page**, input the specified **Object ID** from the list above and followed by the listed **Service Name**.

.. important::
    It is crucial that the **Service Names** within Business Central exactly match with each listed name above.

**10.** Once the web services are added, please click on **Sign in with Microsoft** in the Business Central App.

.. image:: /_static/printscreens/bc/boarding/BC-Boarding6.png

**11.** After the login and authorization process is complete, you will need to provide information about the specific Microsoft Business Central company that you want to integrate with Upsales CRM. 
Do this by following the instructions that are provided on the website.

.. image:: /_static/printscreens/bc/boarding/BC-Boarding7.png

**12.** If everything goes right, you’ll return to the **Business Central App** in Upsales and be able to press **Save**. Once this is done your integration is all set. You should also recieve a notification
in Upsales that the integration has successfully saved its configuration.

.. note::
    Once the integration is installed, we will make sure the provided configuration looks alright before turning on the sync.