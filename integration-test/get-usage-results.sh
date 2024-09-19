set -x #echo on

bq query --use_legacy_sql=false --parameter=commitId:STRING:$SHORT_SHA '
SELECT "The integration tests on commit " || commitId ||
" was executed with a usage of "  || ROUND(cpu_amount,2) || " CPU-Seconds " ||
" and a usage of " || ROUND(memory_amount,2) || " GB-Seconds"
FROM `greenops-demo-env.greenpipeline_metering.usage_metering_per_commitid`
WHERE commitId = "@commitId"
'

bq query --use_legacy_sql=false --parameter=commitId:STRING:$SHORT_SHA '
SELECT 
" Over the previous commit, the CPU usage improved by "  || ROUND(cpu_improvement,2) || " CPU-Seconds " 
" and the memory usage improved by "  || ROUND(mem_improvement,2) || " Memory GB-Seconds " 
  FROM `greenops-demo-env.greenpipeline_metering.commit_usage_impact` 
WHERE commitId = @commitId

'
 