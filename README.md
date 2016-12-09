# fetch module for TorinoMeteo station data

Module used to fetch and parse station data from external urls.

## Usage

Somewhere in your code:

    from fetch.shortcuts import fetch_data

    data = fetch_data(station.data_url, station.data_type.name)
    json_data = data.as_json()

## Submodules

### shortcuts

**fetch_data(url, type): dict**
- url: string
- type: string

fetches, parses and returns data of format type from url

### core

**Data(dict)**
wrapper of the dictionary data type, which adds some convenient methods:

- **as_json(): json**
  returns dictionary in a json format

**fetch(url): string**
- url: string

Fetches and retreives the url content

**parse(content, type): Data**
- content: string
- type: string
Parses the content of format type and retrieves a Data object

### factory

**parser_factory(type): object**
- type: string
Factory method which returns the appropriate parsing class given the content type

### labels

Defines the labels to be used as exported data keys in one place

### parsers.*

All the parser classes, one file for each content type. Same interface, defined by `abstract.Parser`:

**parse(content): dict**
parses content and returns a dictionary of data

## Development

In order to add a parser class:

- add the 'type' condition in the `fetch.factory.parser_factory` function
- add a file in the `fetch.parsers` module implementing the `fetch.parsers.abstract.Parser` interface
