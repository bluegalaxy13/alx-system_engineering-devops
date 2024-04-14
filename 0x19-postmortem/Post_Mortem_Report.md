# Postmortem Report

## 504 Error while accessing a given URL

### Incident report for [504 error / Site Outage](https://github.com/bluegalaxy13/alx-system_engineering-devops/tree/master/0x17-web_stack_debugging_3)

#### Summary

On January 13th, 2024 at midnight the server access went down resulting in 504 error for anyone trying to access a website. Background on the server being based on a LAMP stack.

#### Timeline

- **00:00 PST** - 500 error for anyone trying to access the website
- **00:10 PST** - Ensuring Apache and MySQL are up and running.
- **00:12 PST** - The website was not loading properly which on background check revealed that the server was working properly as well as the database.
- **00:15 PST** - After quick restart to Apache server returned a status of 200 and OK while trying to curl the website.
- **00:18 PST** - Reviewing error logs to check where the error might be coming from.
- **00:25 PST** - Check /var/log to see that the Apache server was being prematurely shut down. The error log for PHP were nowhere to be found.
- **00:33 PST** - Checking php.ini settings revealed all error logging had been turned off. Turning the error logging on.
- **00:35 PST** - Restarting apache server and going to the error logs to check what is being logged into the php error logs.
- **00:40 PST** - Reviewing error logs for php revealed a mistyped file name which was resulting in incorrect loading and premature closing of apache.
- **00:46 PST** - Fixing file name and restarting Apache server.
- **00:50 PST** - Server is now running normally and the website is loading properly.


#### Root Cause and Resolution

The wp-settings.php file's incorrect file name reference was the root of the problem. The server responded with an error code of 500 when the attempt to curl the server was made. It was discovered through reviewing the error logs that no error log file was being written for PHP failures, and there was little information about the server's premature shutdown to be obtained in reading the default error log for Apache. The engineer decided to check the php.ini file's error log settings after realising that the php errors were not being sent anywhere and discovered that all error logging had been disabled. Once turned on, the error logging the apache server was restarted to check if any errors were being registerd in the log. The php log confirmed what was expected: the wp-settings.php file did not contain a file with the.phpp extension. This was obviously a misspelt blunder that caused the site access issue. Since the issue was only discovered in one server, it's possible that it was also duplicated in other servers. Fixing the file extension with puppet would be a simple solution that would also affect other servers. The site and server loaded correctly after a brief deployment of the puppet code that replaced all misspelt file extensions with the correct ones and forced a server restart.

#### Corrective and Preventive Measures

- All servers and sites should have error logging turned on to easily identify errors if anything goes wrong.
- All servers and sites should be tested locally before deploying on a multi-server setup this will result in correcting errors before going live resulting in less fixing time if site goes down.
