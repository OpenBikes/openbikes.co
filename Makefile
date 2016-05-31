# OpenBikes Makefile

## Configuration

BUILD_TIME := $(shell date +%FT%T%z)
PROJECT    := $(shell basename $(PWD))

## Commands

# Install Node JS
install:
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	brew update
	brew upgrade
	brew install node

# Install dependencies
dev:
	npm install

# Launch project
run:
	npm start