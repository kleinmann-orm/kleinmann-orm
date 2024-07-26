# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

### Removed

- Removed Oracle support (`asyncodbc` driver).
- Removed MySQL support (`aiomysql`, `asyncmy` drivers).
- Removed MSSQL support (`asyncodbc` driver).
- Removed `psycopg` driver support.

### Other

- Update `aiosqlite` dependency to `>=0.20.0`.
- Forked pypika-tortoise 0.1.6 as `kleinmann_core`.

## [0.0.1] - 2024-07-24

Initial release. Forked from tortoise-orm 0.21.5.

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html

<!-- Versions -->
[Unreleased]: https://github.com/kleinmann-orm/kleinmann-orm/compare/0.0.1...main
[0.0.1]: https://github.com/kleinmann-orm/kleinmann-orm/compare/bfbbdd1308c5fd1263d50ba2783591e255df30ba...0.0.1
