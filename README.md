# Kleinmann ORM

**Kleinmann ORM** is an async ORM library for Python hardforked from [Tortoise ORM](https://github.com/tortoise/tortoise-orm) and [pypika](https://github.com/tortoise/pypika-tortoise). It's in a very early stage of development and not recommended for general use.

[Project roadmap](https://github.com/kleinmann-orm/kleinmann-orm/issues/2)

Docs are not ready yet; read the code.

## Goals

- Provide a stable codebase for [DipDup framework](https://github.com/dipdup-io/dipdup) which currently relies on a heavily patched Tortoise ORM.
- Integrate our patches into the main codebase to reduce maintenance overhead.
- Merge several stale PRs from the upstream.
- Improve type safety and code quality.
- Reduce the codebase size by reducing the project's scope.

## Breaking changes

Coming from Tortoise ORM as a user or dev? Great! Here's what you need to know.

- Everything named `tortoise` is now `kleinmann`.
- `pypika` code now lives in `kleinmann_core` package.
- MySQL, MSSQL and Oracle databases are no longer supported.
- `psycopg` driver is no longer supported.
- Windows is not supported, but arm64 is.
- Default branch is `main`.

## F.A.Q

### Why Kleinmann?

_(according to [tortoiseknowledge.com](https://www.tortoiseknowledge.com/what-tortoises-stay-small-forever/))_

From a practical and aesthetic standpoint, you can benefit from a small tortoise that’ll:

- **Stay cute forever**: A mini tortoise won’t grow beyond its adorable size, no matter how old it gets.
- **Be easy to handle**: You won’t struggle to hold a little tortoise, and there’s less risk of dropping it.
- **Small enclosure**: Mini tortoises won’t take up much space, even in studio apartments or bedrooms.
- **Eat very little**: Tortoises don’t have big appetites, but mini tortoises require even less to eat.

Some negatives could make a smaller tortoise a bad choice:

- **Less safe for children or pets**: Excited children may hurt this tiny pet by accident, and their shells are less resilient against a playful cat or dog.
- **Safest indoors:** The smaller the tortoise is, the more vulnerable it will be to weather changes and predators. So, you may need to keep your tiny pet tortoise indoors.
- **Expensive to buy when very small**: Common species, like Russian tortoises, may cost a few hundred dollars, while extremely small Egyptian tortoises will cost thousands of dollars.
- **Hard to find:** Super mini tortoises are exotic pets, so they may not be available at all pet stores.
