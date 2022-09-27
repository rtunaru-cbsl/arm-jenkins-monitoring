FROM grafana/grafana:7.5.17

COPY datasources/prometheus.yaml /etc/grafana/provisioning/datasources/
COPY dashboards/dashboard-provider.yaml /etc/grafana/provisioning/dashboards/
COPY dashboards/*.json /var/lib/grafana/dashboards/
