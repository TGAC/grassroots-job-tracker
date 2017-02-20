# Job-Tracker

A simple job status tracker using Django and MongoDB, to provide REST interface for job status.

<p>Using Django and MongoDB</p>


<ul>
    <li><a href="/rest/view_all_jobs">View all jobs in html</a></li>
</ul>

<h2>REST interface</h2>
<h3>GET</h3>
<ul>
    <li>/rest/view_all_jobs (html page for viewing)</li>
    <li>/rest/get_job/job_id</li>
    <li>/rest/update_job?job_uuid=123&amp;status=started</li>

</ul>
<h3>POST</h3>
<ul>
    <li>/rest/update_job/server_id</li>

</ul>

<p>rest interface takes care of timestamp when inserting and updating</p>