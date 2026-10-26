# Model / system card

## Intended use

Retrieve research-method notes, draft a source-linked answer and keep observed evidence separate from interpretation. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Use BM25 over short project-authored method notes carrying links to primary sources. Live mode asks a local LLM for a structured answer and citations; replay mode validates a supplied answer.

## Evaluation protocol

Test unknown source rejection and unsupported questions. Citation identifiers must belong to the retrieved context, and quote spans must occur literally in that source note.

## Known limits

Notes are brief paraphrases rather than a comprehensive literature corpus. Citation validation does not prove scientific entailment or consensus, and generated answers are not medical advice.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Ingest licensed full texts with versioned provenance, compare lexical and semantic retrieval, label claim support and evaluate contradictory sources.
