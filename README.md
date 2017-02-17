# Job-Tracker

A simple job status tracker using Django and MongoDB, to provide REST interface for job status.

<h1>REST interface</h1>
<h2>GET</h2>
<ul>
    <li>/rest/view_all_job</li>
    <li>/rest/insert_job?job_uuid=123&amp;status=started</li>
    <li>/rest/get_job?job_uuid=123</li>
    <li>/rest/update_job?job_uuid=123&amp;status=started</li>

</ul>

<p>rest interface takes care of timestamp when inserting and updating</p>