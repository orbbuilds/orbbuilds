# baseline vs v1-single

19 tasks in both runs. Metric: task_complete.

| | baseline | v1-single | change |
| --- | ---: | ---: | ---: |
| tasks complete | 4.0/19 (21%) | 13.0/19 (68%) | +9.0 |
| latency per task (s) | 26.8 | 12.4 | -54% |
| model calls per task | 7.0 | 2.8 | -60% |
| input tokens per task | 3,548 | 1,805 | -49% |
| output tokens per task | 384 | 159 | -59% |

## Tasks that changed

| task | baseline | v1-single | tags |
| --- | ---: | ---: | --- |
| t08 | 1/2 | 0/2 | account |
| t14 | 2/2 | 1/2 | break-check, lost-rule, account |
| t01 | 0/2 | 1/2 | orders+shipping |
| t02 | 0/2 | 2/2 | orders+shipping |
| t03 | 1/2 | 2/2 | orders+shipping |
| t04 | 0/2 | 2/2 | returns |
| t05 | 0/2 | 2/2 | returns |
| t06 | 1/2 | 2/2 | returns |
| t07 | 1/2 | 2/2 | account |
| t09 | 0/2 | 1/2 | diagnostics |
| t10 | 1/2 | 2/2 | claims, multi-turn |
| t12 | 0/2 | 1/2 | cross-domain, diagnostics, orders+shipping |
| t13 | 0/2 | 2/2 | break-check, chain, account, returns |
| t16 | 0/2 | 2/2 | break-check, unhappy-path, diagnostics |
| t17 | 0/2 | 2/2 | break-check, multi-turn, returns |
| t19 | 1/2 | 2/2 | break-check, unhappy-path, diagnostics |

## Writes that changed

What each task changed in the systems, per rep. A slash separates reps that differ.

| task | baseline | v1-single |
| --- | --- | --- |
| t04 | none | create_return |
| t05 | none / set_marketing_opt_in | none |
| t07 | update_shipping_address / none | update_shipping_address |
| t08 | set_marketing_opt_in | set_marketing_opt_in / none |
| t10 | open_claim | create_return, open_claim, open_claim / open_claim, open_claim |
| t11 | none | create_return |
| t13 | create_return / create_return, update_shipping_address | create_return, update_shipping_address |
| t14 | none | update_shipping_address / none |
| t15 | create_return / none | create_return |
| t17 | none | create_return |

## Paths that changed

Reps of a task in which an agent was called. A task can keep its score and still take a different route.

| task | agent | baseline | v1-single |
| --- | --- | ---: | ---: |
| t01 | main | 0/2 | 2/2 |
| t01 | orders | 2/2 | 0/2 |
| t01 | router | 2/2 | 0/2 |
| t02 | main | 0/2 | 2/2 |
| t02 | orders | 2/2 | 0/2 |
| t02 | router | 2/2 | 0/2 |
| t02 | shipping | 2/2 | 0/2 |
| t03 | main | 0/2 | 2/2 |
| t03 | router | 2/2 | 0/2 |
| t04 | main | 0/2 | 2/2 |
| t04 | router | 2/2 | 0/2 |
| t05 | main | 0/2 | 2/2 |
| t05 | router | 2/2 | 0/2 |
| t06 | main | 0/2 | 2/2 |
| t06 | router | 2/2 | 0/2 |
| t07 | main | 0/2 | 2/2 |
| t07 | router | 2/2 | 0/2 |
| t08 | account | 2/2 | 0/2 |
| t08 | claims | 2/2 | 0/2 |
| t08 | main | 0/2 | 2/2 |
| t08 | router | 2/2 | 0/2 |
| t09 | main | 0/2 | 2/2 |
| t09 | router | 2/2 | 0/2 |
| t10 | main | 0/2 | 2/2 |
| t10 | router | 2/2 | 0/2 |
| t11 | main | 0/2 | 2/2 |
| t11 | returns | 2/2 | 0/2 |
| t11 | router | 2/2 | 0/2 |
| t12 | main | 0/2 | 2/2 |
| t12 | router | 2/2 | 0/2 |
| t13 | main | 0/2 | 2/2 |
| t13 | returns | 2/2 | 0/2 |
| t13 | router | 2/2 | 0/2 |
| t14 | claims | 2/2 | 0/2 |
| t14 | main | 0/2 | 2/2 |
| t14 | router | 2/2 | 0/2 |
| t15 | claims | 2/2 | 0/2 |
| t15 | main | 0/2 | 2/2 |
| t15 | returns | 2/2 | 0/2 |
| t15 | router | 2/2 | 0/2 |
| t16 | diagnostics | 2/2 | 0/2 |
| t16 | main | 0/2 | 2/2 |
| t16 | router | 2/2 | 0/2 |
| t17 | main | 0/2 | 2/2 |
| t17 | returns | 2/2 | 0/2 |
| t17 | router | 2/2 | 0/2 |
| t18 | main | 0/2 | 2/2 |
| t18 | router | 2/2 | 0/2 |
| t19 | diagnostics | 2/2 | 0/2 |
| t19 | main | 0/2 | 2/2 |
| t19 | router | 2/2 | 0/2 |

One rep apart, which the unchanged system often does by itself: t03 (orders), t04 (orders), t04 (returns), t04 (shipping), t05 (account), t05 (orders), t05 (returns), t05 (shipping), t06 (orders), t06 (returns), t07 (account), t09 (claims), t09 (diagnostics), t10 (orders), t11 (claims), t13 (account), t13 (claims), t13 (diagnostics), t13 (orders), t13 (shipping), t17 (account), t17 (diagnostics), t17 (orders), t17 (shipping), t18 (claims).

## By tag

| tag | baseline | v1-single |
| --- | ---: | ---: |
| account | 4/8 | 5/8 |
| break-check | 3/14 | 9/14 |
| chain | 0/2 | 2/2 |
| claims | 1/2 | 2/2 |
| cross-domain | 0/4 | 1/4 |
| diagnostics | 1/10 | 6/10 |
| lost-rule | 2/2 | 1/2 |
| multi-turn | 1/6 | 4/6 |
| orders+shipping | 1/10 | 6/10 |
| returns | 1/14 | 10/14 |
| unhappy-path | 1/4 | 4/4 |
| wrong-pick | 0/2 | 0/2 |

## By agent, per task

| agent | calls, baseline | calls, v1-single | input tokens, baseline | input tokens, v1-single |
| --- | ---: | ---: | ---: | ---: |
| account | 0.3 | 0.0 | 81 | 0 |
| claims | 0.8 | 0.3 | 311 | 147 |
| diagnostics | 0.7 | 0.3 | 261 | 95 |
| main | 0.0 | 2.2 | 0 | 1,563 |
| orders | 0.7 | 0.0 | 177 | 0 |
| returns | 1.1 | 0.0 | 451 | 0 |
| router | 3.0 | 0.0 | 2,159 | 0 |
| shipping | 0.4 | 0.0 | 107 | 0 |

## Verdict

**v1-single scores the same or better overall, but got worse on t08, t14.** Read those traces before keeping the change.

Notes:

- Writes differ on t04, t05, t07, t08, t10, t11, t13, t14, t15, t17. Check each one is a write the task wanted. A task can pass its checks and still change something it should not.
- The route changed on t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19. Where the change was not meant to touch a task, read its trace even if the score held, and say what the new route costs.
- Model for both runs: llama3.2.
- Changed in a single rep: t08, t14, t01, t03, t06, t07, t09, t10, t12, t19. That can be noise. Treat it as real only if the trace shows a cause.
