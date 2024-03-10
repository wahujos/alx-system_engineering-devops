On Friday last week on the 8th of march 2024, we experienced challenges with most of the clients using our apache server complaining that they could not be able to access their websites. Today we are providing an incident report detailing the nature of the issue and our response. 
Issue Summary

From 4:00 PM to 5:30 PM EAT, users using our apache servers were not able to access their websites always receiving a 500 error response message.Our own websites that rely on the server also were not accessible.The root cause of this issue was an invalid configuration change that exposed a bug.

Timeline (all times East African Time)
3:50 PM. Configuration push begins
4:00 PM issue arises
4:00 PM Pagers alerted the team
4:10 PM Troubleshooting of the server
4:40 PM identified the problem with the server and fixed it
4:50 PM server restart begins
5:00 PM users websites become accessible
5:30 PM: 100% of the users could access their websites.

Root Cause

At 3:50 PM, a change was pushed to the server involving the settings of the server. The change caused a 500 error that made the server not to be accessible. This was caused by a wrong extension in the setting file that changed the configuration of the server.

Resolution and Recovery

The issue was brought to the attention of the software engineers through an alert made from the Pagers. The team worked on troubleshooting the error and realised the settings file was not well configured. They returned the setting files to default and this corrected the extension issue that had been realised.

Corrective and Preventive measure

We have been able to add up more servers to act as backup. This will help prevent users from failing to access their websites in case one server is down. We have also come up with measures that allow for testing of any changes made before they are pushed to production.

We would sincerely take this opportunity to apologize to our users for any inconvenience caused and assure them that we are more equipped to handle any error that appear in future. Thanks for doing business with us. 

Sincerely, 
Hosting Company.



