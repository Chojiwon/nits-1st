from channels import include

channel_routing = [
    include('blog.routing.channel_routing', path=r'^/blog/'),
]

