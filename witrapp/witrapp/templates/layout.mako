<!DOCTYPE html>
<html>
<head>
<meta charset ="UTF-8">
    <title>OR Online</title>
    <meta name="keywords" content="pyramid web application" />
    <meta name="discription" content="pyramid web application" />
    <link rel="shortcut icon" href="${request.static_path('witrapp:static/favicon.ico')}" />
    <link rel="stylesheet" href="${request.static_path('witrapp:static/css/bootstrap.css')}" type="text/css" media="screen" charset="utf-8" />
    <!--[if lte IE 6]>
    <link rel="stylesheet" href="${request.static_path('witrapp:static/ie6.css')}"  charset="utf-8" />
    <![endif]-->
</head>
<body>
<div class="container">
    ${next.body()}
</div>
</body>
</html>
