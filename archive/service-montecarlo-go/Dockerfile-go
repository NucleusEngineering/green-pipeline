FROM golang:1.19
WORKDIR /service
COPY *.go ./
# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /service-montecarlo
EXPOSE 8080
CMD ["/service-montecarlo"]