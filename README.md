# Job-Tracker
<p>A simple job status tracker using Django and MongoDB, to provide REST interface for job status. Using Django and MongoDB</p>


<h2>REST interface</h2>
<h3>GET</h3>
<ul>
    <li>/rest/get_jobs</li>
    <li>/rest/get_job/job_id</li>

</ul>
<h3>POST</h3>
<ul>
    <li>/rest/update_job/server_id</li>

</ul>

<p>rest interface takes care of timestamp when inserting and updating</p>

<h2>HTML view</h2>

<p>Using jQuery and DataTable</p>

<p><a href="/view_jobs">View all jobs in html</p>