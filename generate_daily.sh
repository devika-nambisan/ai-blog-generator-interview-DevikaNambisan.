#!/bin/bash
KEYWORD="wireless earbuds"
curl "http://localhost:5000/generate?keyword=${KEYWORD}" -o "blog_posts/$(date +%F)_${KEYWORD// /_}.json"
