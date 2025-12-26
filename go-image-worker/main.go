

package main

import (
    "fmt"
    "image"
    "image/color"
    "image/png"
    "math/rand"
    "net/http"
    "os"
    "runtime"
    "time"
)

var memoryHog [][]byte

func generateImage(width, height int) *image.RGBA {
    img := image.NewRGBA(image.Rect(0, 0, width, height))
    for y := 0; y < height; y++ {
        for x := 0; x < width; x++ {
            img.Set(x, y, color.RGBA{
                R: uint8(rand.Intn(256)),
                G: uint8(rand.Intn(256)),
                B: uint8(rand.Intn(256)),
                A: 255,
            })
        }
    }
    return img
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    fmt.Fprintf(w, `{"status":"healthy","goroutines":%d}`, runtime.NumGoroutine())
}

func lightLoadHandler(w http.ResponseWriter, r *http.Request) {
    start := time.Now()
    fmt.Println("📊 Light load started")
    
    // Generate 1 small image
    img := generateImage(500, 500)
    
    // Save to temp file
    f, _ := os.CreateTemp("", "image-*.png")
    defer os.Remove(f.Name())
    png.Encode(f, img)
    f.Close()
    
    duration := time.Since(start)
    fmt.Printf("✅ Light load completed in %v\n", duration)
    
    w.Header().Set("Content-Type", "application/json")
    fmt.Fprintf(w, `{"status":"completed","duration":"%v","images":1}`, duration)
}

func mediumLoadHandler(w http.ResponseWriter, r *http.Request) {
    start := time.Now()
    fmt.Println("📊 Medium load started")
    
    // Generate 5 medium images
    for i := 0; i < 5; i++ {
        img := generateImage(1000, 1000)
        f, _ := os.CreateTemp("", "image-*.png")
        png.Encode(f, img)
        f.Close()
        os.Remove(f.Name())
    }
    
    duration := time.Since(start)
    fmt.Printf("✅ Medium load completed in %v\n", duration)
    
    w.Header().Set("Content-Type", "application/json")
    fmt.Fprintf(w, `{"status":"completed","duration":"%v","images":5}`, duration)
}

func heavyLoadHandler(w http.ResponseWriter, r *http.Request) {
    start := time.Now()
    fmt.Println("🔥 Heavy load started")
    
    // Generate 10 large images (CPU + Memory intensive)
    for i := 0; i < 10; i++ {
        img := generateImage(2000, 2000)
        f, _ := os.CreateTemp("", "image-*.png")
        png.Encode(f, img)
        f.Close()
        os.Remove(f.Name())
    }
    
    duration := time.Since(start)
    fmt.Printf("✅ Heavy load completed in %v\n", duration)
    
    w.Header().Set("Content-Type", "application/json")
    fmt.Fprintf(w, `{"status":"completed","duration":"%v","images":10}`, duration)
}

func memoryLeakHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Println("💾 Allocating 50MB memory")
    
    // Allocate 50MB and keep it
    chunk := make([]byte, 50*1024*1024)
    for i := range chunk {
        chunk[i] = byte(i % 256)
    }
    memoryHog = append(memoryHog, chunk)
    
    var m runtime.MemStats
    runtime.ReadMemStats(&m)
    
    fmt.Printf("✅ Memory allocated. Total: %d MB\n", m.Alloc/1024/1024)
    
    w.Header().Set("Content-Type", "application/json")
    fmt.Fprintf(w, `{"status":"allocated","memory_mb":%d}`, m.Alloc/1024/1024)
}

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Go Image Worker API\n")
    })
    
    http.HandleFunc("/health", healthHandler)
    http.HandleFunc("/light", lightLoadHandler)
    http.HandleFunc("/medium", mediumLoadHandler)
    http.HandleFunc("/heavy", heavyLoadHandler)
    http.HandleFunc("/memory-leak", memoryLeakHandler)
    
    fmt.Println("🚀 Go Image Worker running on port 8080")
    http.ListenAndServe(":8080", nil)
}


