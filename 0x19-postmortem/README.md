# Postmortem

Acquiring the skill of writing an incident report, which is also called a postmortem. The rules that Google engineers strictly adhere to when filing reports are followed in this postmortem. The report is divided into five sections: an overview of the problem, a timeline, an analysis of the root cause, a resolution and recovery plan, and finally, corrective and preventive actions. Let's take a closer look at each of these sections.

### Issue Summary

- short summary (5 sentences)
- list the duration along with start and end times (include timezone)
- state the impact (most user requests resulted in 500 errors, at peak 100%)
- close with root cause

### Timeline

- list the timezone
- covers the outage duration
- when outage began
- when staff was notified
- actions, events, …
- when service was restored

### Root Cause

- give a detailed explanation of event
- do not sugarcoat

### Resolution and recovery

- give detailed explanation of actions taken (includes times)

### Corrective and Preventative Measures

- itemized list of ways to prevent it from happening again
- what can we do better next time?
