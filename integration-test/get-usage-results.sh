bq query --nouse_legacy_sql --parameter commitId:STRING:$SHORT_SHA \
'SELECT "The integration tests on commit " || commitId ||
" was executed with a usage of "  || cpu_amount || " CPU-Seconds " ||
" and a usage of " || memory_amount || " GB-Seconds"

FROM 
`greenops-demo-env.greenpipeline_metering.usage_metering_per_commitid`
WHERE commitId = "@commitId"
'
