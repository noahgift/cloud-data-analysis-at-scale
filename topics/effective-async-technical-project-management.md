## Effective Async Technical Project Management

### Why Software Projects Fail

It is common for software projects to fail.  Working in the Bay Area over a decade I saw more failed projects than successful projects.  Here is what most likely goes wrong:

* Lack of automation
* Lack of effective project management process
* HIPPOs (Highest Paid Person's Opinion) and Heros let everyone down.  This is another way of saying *EGO IS THE PROCESS*.
* Lack of effective technical management
* Lack of experience building software that works and is on-time
* Overconfidence
* Failing in love with complexity of any kind
* Lack of teamwork

### How to ship high quality software that works and is on-time

One method of hitting a deadline is creating a plan to hit the deadline.  Here is a checklist:

1.  Start with automation.   Before the first line of code is written hook it up to a [SaaS build system that lints and tests the code](https://circleci.com/blog/increase-reliability-in-data-science-and-machine-learning-projects-with-circleci/).
2. Create a quarterly and yearly plan on a spreadsheet.  Take a guess at the week by week deliverables. Estimate difficulty or time or both for each task.
3. Create a simple Board based flow:  To Do, In Progress, Done. Friday is a good day to schedule due dates, and Monday is a good day to do a quick "demo".

![trello](https://user-images.githubusercontent.com/58792/72353262-bf9bee00-36b1-11ea-9268-628bc9f483a7.png)

4.  Always demo, every monday.  The code has to work and be of the same quality as the final project.
5.  Never work until the deadline.  For a major deadline, assume at least a couple of weeks of QA or being late.
6.  Be on the constant lookup for complexity and reduce it.  If there is a choice because two tasks and one is more complex, do the simple version.
7.  Create an effective team which values process over ego.  You can read more about teamwork generally in [Teamwork:  What Must Go Right/What Can Go Wrong](https://www.amazon.com/Teamwork-Right-Wrong-Interpersonal-Communication/dp/0803932901) and the last chapter of [Python for DevOps](https://www.amazon.com/dp/149205769X/).
8.  Embrace YAGNI (You Ain't Gonna Need It).

### Other examples of high failure undertakings

The same software project management principles can  

* Diets

Diets, counting calories and other complex schemes don't work.  Effective automation heuristics like [intermittent fasting do](https://noahgift.com/articles/datascience-meets-intermittent-fasting/).  Why does IF work?  There is nothing to remember or reason about.  It is a simple heuristic for a complex problem.

* Exercise and Fitness

Unrealistic goals and overly complex plans create failure.  Automation creates compliance.  Most people brush their teeth every morning.  Why?  The intellectual complexity is low and it is a habit.  A daily morning walk is an example of a simple form of automation with 100% success.

* Saving money

What works is automation.  Passive investment and passive savings.  Humans are biased and make mistakes, but automation is forever.

* Writing books

Writing a book is just like building software.  Many people fail at writing books because of exploding complexity and lack of automation.  What is done last week is what will be done the next week.

### Exercises 

* Topic: Create technical project plan for final project
* Directions:  

    - Part A:  With your project team, create an approximately 12 week schedule with "two-weeks" of QA built in.  Use a spreadsheet for this.  This means you have to effectively stop creating features and test for the final two weeks.  This equates to 10 weeks of coding max.

    - Part B:  Create a ticket system using [Github](https://github.com/), [Trello](http://trello.com/), or [Jira](https://www.atlassian.com/software/jira).  *Warning...the only thing worth than no ticket system is a ticket system that explodes with so much complexity it is unusable.  This is MUCH worse! Embrace K.I.S.S.*

    - Part C:  Create an internal "weekly demo" schedule and invite team to it.  Make sure it is brief and working code is demo'd each week.  Adjust schedule as you encounter issues.

    - Part D:  "Demo" your setup to class.


