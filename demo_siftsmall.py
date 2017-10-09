import pqtable

# (1) Make sure you have already downloaded siftsmall data in data/ by scripts/download_siftsmall.sh

# (2) Read vectors

queries = pqtable.ReadTopN("data/siftsmall/siftsmall_query.fvecs", "fvecs")  # Because top_n is not set, read all vectors
bases = pqtable.ReadTopN("data/siftsmall/siftsmall_base.fvecs", "fvecs")
learns = pqtable.ReadTopN("data/siftsmall/siftsmall_learn.fvecs", "fvecs")

# (3)Train a product quantizer int
M = 4
print("=== Train a product quantizer ===")
pq = pqtable.PQ(pqtable.PQ.Learn(learns, M))

# (4) Encode vectors to PQ - codes
print("=== Encode vectors into PQ codes ===")
codes = pq.Encode_Array(bases)

# (5) Build a PQTable
print("=== Build PQTable ===")
tbl = pqtable.PQTable(pq.GetCodewords(), codes)

# (6) Do search
print("=== Do search ===")
t0 = pqtable.Elapsed()

for q, query in enumerate(queries):
    result = tbl.Query(query)  # result = (nearest_id, its_dist)
    print(str(q) + "th query: nearest_id=" + str(result[0]) + ", dist=" + str(result[1]))

print(str((pqtable.Elapsed() - t0) / len(queries) * 1000) + " [msec/query]")
