FROM golang:1.19
WORKDIR /service
COPY *.go ./
# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping
EXPOSE 8080
CMD ["/docker-gs-ping"]