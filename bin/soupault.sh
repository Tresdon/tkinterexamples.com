#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        bin/linux/soupault
elif [[ "$OSTYPE" == "darwin"* ]]; then
        bin/osx/soupault
fi;