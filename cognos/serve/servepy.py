import http.server
"""
usage:
    >>>python -m http.server
    >Serving HTTP on 0.0.0. port 8000
        >>>curl localhost:8000

    >>> python -m http.server --bind 127.0.0.1
"""





"""
docker:
    docker loopback -- how to navigate docker networking to allow connections to the host machine localhost
        instead of the in-container localhost
        docker run --add-host host.docker.internal:host-gateway --rm -ti mycontainer bash
            >>>cat /etc/hosts
            >host.docker.internal
                >>>curl host.docker.internal:8000 == >>>curl localhost:8000 #outside the docker container
    >>>docker network inspect bridge --format='{{index .IPAM.Config 0).Gateway}}'
        >inspect the docker bridge network for its gateway ip address
    ### We need to bind our server to the result of the docker bridge inspection above:
        >>>python -m http.server --bind "docker bridge network ip from above"
"""

