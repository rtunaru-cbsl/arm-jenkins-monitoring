FROM jenkins/jenkins:2.332.3-lts

# Add Jenkins init files
COPY src/ /usr/share/jenkins/ref/

COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
