#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        bin/linux/cmark --unsafe --smart $1
elif [[ "$OSTYPE" == "darwin"* ]]; then
        bin/osx/cmark --unsafe --smart $1
fi;