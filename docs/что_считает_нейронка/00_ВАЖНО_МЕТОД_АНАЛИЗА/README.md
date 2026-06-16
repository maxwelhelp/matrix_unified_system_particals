# 00 — ВАЖНО: метод анализа

Это самая важная папка направления **«что считает нейронка»**.

Её надо читать первой, до любых отдельных отчётов.

## Почему она важна

Главная ошибка, которую мы уже совершали:

```text
смотреть только route/head/activation и забывать спросить:
что это физически или логически означает?
```

Правильный порядок:

```text
1. найти систематическую ошибку / аномалию
2. понять физический/данный смысл классов
3. сравнить confused vs correct
4. найти monotonic observable
5. проверить patch/control
6. построить surrogate
7. если surrogate ошибается — искать veto/additional trigger
```

## Главный документ

```text
REASONING_FRAMEWORK_V1.md
```

Этот framework создан из логики, которая привела нас от head/route tracing к реальному finding:

```text
ParticleNet uses lepton/core isolation inside jet for Hqql/Tbl ambiguity.
```

## Запомнить

```text
Не “какая голова активна?”
А “какой физический/логический observable она считает?”
```

## Автоматизация

Все будущие анализаторы отчётов должны следовать этому framework:

```text
confusion -> contrastive groups -> bins/monotonicity -> patch -> surrogate -> residual inversion
```
