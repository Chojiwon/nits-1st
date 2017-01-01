from channels import route, include

channel_routing = [
    include('blog.routing.channel_routing', path=r'^/blog/'),
]

