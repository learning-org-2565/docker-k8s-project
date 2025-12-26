FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod .
COPY main.go .
RUN go build -o go-image-worker main.go

# 2nd stage -build the app
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/go-image-worker .
EXPOSE 8080
CMD ["./go-image-worker"]

#so this is a multi stage dockerfile where we have two pahses,
# 1st we are creating build image where creating work dir, coping the dep and source code
# then building the go binary , this is executable file , it can be run on any linux machine
# 2nd stage we are creating a small image using alpine where we creating work dir and then copying the binaries from buider stage
# finally exposing the port and running the binary only directly 