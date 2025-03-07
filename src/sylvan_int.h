/*
 * Copyright 2011-2016 Formal Methods and Tools, University of Twente
 * Copyright 2016-2017 Tom van Dijk, Johannes Kepler University Linz
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Sylvan: parallel MTBDD/ListDD package.
 * Include this file for access to internals.
 */

#include <sylvan.h>

#ifdef __cplusplus
namespace sylvan {
#endif

/**
 * Sylvan internal header files inside the namespace
 */

#include <sylvan_cache.h>
#include <sylvan_table.h>
#include <sylvan_hash.h>

#ifndef SYLVAN_INT_H
#define SYLVAN_INT_H

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

/**
 * Nodes table.
 */
extern llmsset_t nodes;

/**
 * Macros for all operation identifiers for the operation cache
 */

// BDD operations
static const uint64_t CACHE_BDD_ITE                 = (0LL<<40);
static const uint64_t CACHE_BDD_AND                 = (1LL<<40);
static const uint64_t CACHE_BDD_XOR                 = (2LL<<40);
static const uint64_t CACHE_BDD_EXISTS              = (3LL<<40);
static const uint64_t CACHE_BDD_PROJECT             = (4LL<<40);
static const uint64_t CACHE_BDD_AND_EXISTS          = (5LL<<40);
static const uint64_t CACHE_BDD_AND_PROJECT         = (6LL<<40);
static const uint64_t CACHE_BDD_RELNEXT             = (7LL<<40);
static const uint64_t CACHE_BDD_RELPREV             = (8LL<<40);
static const uint64_t CACHE_BDD_SATCOUNT            = (9LL<<40);
static const uint64_t CACHE_BDD_COMPOSE             = (10LL<<40);
static const uint64_t CACHE_BDD_RESTRICT            = (11LL<<40);
static const uint64_t CACHE_BDD_CONSTRAIN           = (12LL<<40);
static const uint64_t CACHE_BDD_CLOSURE             = (13LL<<40);
static const uint64_t CACHE_BDD_ISBDD               = (14LL<<40);
static const uint64_t CACHE_BDD_SUPPORT             = (15LL<<40);
static const uint64_t CACHE_BDD_PATHCOUNT           = (16LL<<40);

// MDD operations
static const uint64_t CACHE_MDD_RELPROD             = (20LL<<40);
static const uint64_t CACHE_MDD_MINUS               = (21LL<<40);
static const uint64_t CACHE_MDD_UNION               = (22LL<<40);
static const uint64_t CACHE_MDD_INTERSECT           = (23LL<<40);
static const uint64_t CACHE_MDD_PROJECT             = (24LL<<40);
static const uint64_t CACHE_MDD_JOIN                = (25LL<<40);
static const uint64_t CACHE_MDD_MATCH               = (26LL<<40);
static const uint64_t CACHE_MDD_RELPREV             = (27LL<<40);
static const uint64_t CACHE_MDD_SATCOUNT            = (28LL<<40);
static const uint64_t CACHE_MDD_SATCOUNTL1          = (29LL<<40);
static const uint64_t CACHE_MDD_SATCOUNTL2          = (30LL<<40);

// MTBDD operations
static const uint64_t CACHE_MTBDD_APPLY             = (40LL<<40);
static const uint64_t CACHE_MTBDD_UAPPLY            = (41LL<<40);
static const uint64_t CACHE_MTBDD_ABSTRACT          = (42LL<<40);
static const uint64_t CACHE_MTBDD_ITE               = (43LL<<40);
static const uint64_t CACHE_MTBDD_AND_ABSTRACT_PLUS = (44LL<<40);
static const uint64_t CACHE_MTBDD_AND_ABSTRACT_MAX  = (45LL<<40);
static const uint64_t CACHE_MTBDD_SUPPORT           = (46LL<<40);
static const uint64_t CACHE_MTBDD_COMPOSE           = (47LL<<40);
static const uint64_t CACHE_MTBDD_EQUAL_NORM        = (48LL<<40);
static const uint64_t CACHE_MTBDD_EQUAL_NORM_REL    = (49LL<<40);
static const uint64_t CACHE_MTBDD_MINIMUM           = (50LL<<40);
static const uint64_t CACHE_MTBDD_MAXIMUM           = (51LL<<40);
static const uint64_t CACHE_MTBDD_LEQ               = (52LL<<40);
static const uint64_t CACHE_MTBDD_LESS              = (53LL<<40);
static const uint64_t CACHE_MTBDD_GEQ               = (54LL<<40);
static const uint64_t CACHE_MTBDD_GREATER           = (55LL<<40);
static const uint64_t CACHE_MTBDD_EVAL_COMPOSE      = (56LL<<40);
static const uint64_t CACHE_MTBDD_MATVEC_MULT       = (57LL<<40);
static const uint64_t CACHE_MTBDD_MATMAT_MULT       = (58LL<<40);
static const uint64_t CACHE_MTBDD_RENUMBER_VARS     = (59LL<<40);
static const uint64_t CACHE_MTBDD_TOPVAR            = (60LL<<40);
static const uint64_t CACHE_MTBDD_TENSOR            = (61LL<<40);
static const uint64_t CACHE_MTBDD_GETNORM_MPC       = (62LL<<40);


// EVBDD operations
static const uint64_t CACHE_EVBDD_PLUS               = (70LL<<40);
static const uint64_t CACHE_EVBDD_MATVEC_MULT        = (71LL<<40);
static const uint64_t CACHE_EVBDD_MATMAT_MULT        = (72LL<<40);
static const uint64_t CACHE_EVBDD_INPROD             = (73LL<<30);
static const uint64_t CACHE_EVBDD_REPLACE_TERMINAL   = (74LL<<40);
static const uint64_t CACHE_EVBDD_INC_VARS           = (75LL<<40);
static const uint64_t CACHE_EVBDD_CLEAN_WGT_TABLE    = (76LL<<40);
static const uint64_t CACHE_EVBDD_IS_ORDERED         = (77LL<<40);

// Operations on EVBDD edge weights
static const uint64_t CACHE_WGT_ADD                 = (80LL<<40);
static const uint64_t CACHE_WGT_SUB                 = (81LL<<40);
static const uint64_t CACHE_WGT_MUL                 = (82LL<<40);
static const uint64_t CACHE_WGT_DIV                 = (83LL<<40);

// QMDD operations
static const uint64_t CACHE_QMDD_GATE               = (90LL<<40);
static const uint64_t CACHE_QMDD_CGATE              = (91LL<<40);
static const uint64_t CACHE_QMDD_CGATE_RANGE        = (92LL<<40);
static const uint64_t CACHE_QMDD_SUBCIRC            = (93LL<<40);
static const uint64_t CACHE_QMDD_PROB               = (94LL<<40);

// TODO: renumber

// ZDD operations
static const uint64_t CACHE_ZDD_FROM_MTBDD          = (100LL<<40);
static const uint64_t CACHE_ZDD_TO_MTBDD            = (101LL<<40);
static const uint64_t CACHE_ZDD_EXTEND_DOMAIN       = (102LL<<40);
static const uint64_t CACHE_ZDD_SUPPORT             = (103LL<<40);
static const uint64_t CACHE_ZDD_PATHCOUNT           = (104LL<<40);
static const uint64_t CACHE_ZDD_AND                 = (105LL<<40);
static const uint64_t CACHE_ZDD_OR                  = (106LL<<40);
static const uint64_t CACHE_ZDD_ITE                 = (107LL<<40);
static const uint64_t CACHE_ZDD_NOT                 = (108LL<<40);
static const uint64_t CACHE_ZDD_DIFF                = (109LL<<40);
static const uint64_t CACHE_ZDD_EXISTS              = (110LL<<40);
static const uint64_t CACHE_ZDD_PROJECT             = (111LL<<40);
static const uint64_t CACHE_ZDD_ISOP                = (112LL<<40);
static const uint64_t CACHE_ZDD_COVER_TO_BDD        = (113LL<<40);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#include <sylvan_evbdd_int.h>
#include <sylvan_mtbdd_int.h>
#include <sylvan_ldd_int.h>
#include <sylvan_zdd_int.h>

#ifdef __cplusplus
} /* namespace */
#endif

#endif
