# Kleinmann ORM

**Kleinmann ORM** is an async ORM library for Python hardforked from [Tortoise ORM](https://github.com/tortoise/tortoise-orm). It's in a very early stage of development and not recommended for general use.

## Goals

- Provide a stable codebase for [DipDup framework](https://github.com/dipdup-io/dipdup) which currently relies on a heavily patched Tortoise ORM.
- Integrate our patches into the main codebase to reduce maintenance overhead.
- Merge several stale PRs from the upstream.
- Improve type safety and code quality.
- Reduce the codebase size by reducing the project's scope.

Maintaining compatibility with Tortoise ORM is not a goal, but we will try to keep a list of breaking changes in the documentation.

Project roadmap: https://github.com/kleinmann-orm/kleinmann-orm/issues/2
