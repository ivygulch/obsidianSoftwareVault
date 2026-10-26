# Southampton Fire Department Calendar App Project

Prepared by Doug Sjoquist · dwsjoquist@ivygulch.com · August 27, 2026

Chief,

Jason showed me a few screenshots of the application your department currently uses to give me a general idea of what your needs are. The general requirements I took from the call were:
- a private calendar app for departmental events, reminders, and attendance status
- viewable by all members
- editable from a mobile phone by individuals with appropriate admin rights
## The options, briefly

Before considering custom software, it is usually a good idea to survey what is available on the market. Even if you pursue the custom path, other applications can help guide what you have built. The existing offerings I found fall into two broad categories: general group communication apps and fire-department-specific ones.

**Free group apps**
- **BAND** (free) — private group calendar with RSVPs and reminders, plus a built-in printable monthly calendar for the station wall. It is not clear what attendance status features are available.
- **TeamSnap** (~$120/yr) — a paid and ad-supported app that does have the three statuses desired: Yes / No / Maybe
- **Spond** (free) — solid events and reminders, but no "possible" status
- **Google Calendar** (free) — some of your needs could be met through Google's tools, but probably not everything

**Fire-department platforms**
- **IamResponding** (from ~$349/yr)
- **Responserack** ($300–720/yr)
- **Station Boss** (from $1,800/yr) 
- All include an events calendar, but as one module of a records/alerting system that goes beyond this need. 

**A custom-built app**
- matched exactly to the need
- the trade-offs: 
	- real upfront cost and a few months to v1.0
	- decisions about how to handle ongoing maintenance

It might be worth trying one of the free options (or free trials) before pursuing a custom build.
## High-level questions related to custom application development

These shape the decision more than any feature list:

1. **What's making this worth doing now?** 
   What keeps going wrong with the current setup, and is there a date this needs to work by?
2. **What does a typical month of department activity look like?** 
   What kinds of events are there?
   Who announces them?
   How do members hear about them today?
3. **When members answer committed / possible / can't make it — what do you do with that count?** 
   Call more people, cancel, confirm a minimum crew? 
   Is "who hasn't answered" as important as who has?
4. **Who is the least tech-comfortable member this has to work for?** 
   What phone do they carry? 
   Would they install an app?
5. **What has to exist on paper or on a wall?** 
   Is a printed monthly calendar at the station (or in trucks) part of how the department runs out of necessity or desire?
6. **Does anything else depend on this calendar?** 
   Training-hour records, LOSAP, township reports?
   Does someone retype calendar information into something else today?
7. **A year in, who's running it?** 
   Who adds members, fixes a wrong event, and answers questions — and what happens when that person's term ends?
8. **What would make this a success or failure a year from now?** 
   Has the department tried tools that didn't stick? If so, why didn't they?
