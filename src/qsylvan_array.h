/*
 * Copyright 2023-2025 System Verification Lab, LIACS, Leiden University.
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
 * 
 * Author: Richard M.K. van Dijk, RSE @ LIACS.
 * 
 */

/**
 * This module contains matrix.matrix and matrix.vector multiplications, array based.
 * 
 * It is used for the unit test functions to test the MTBDD QSylvan functions.
 * 
 * It also contains conversion functions from array to MTBDD and verse versa:
 *
 * Convert a matrix array M[row][col] into a MTBDD.
 * 
 * Convert a vector array v[row] into a MTBDD.
 * 
 * Convert a MTBDD into a matrix array.
 * 
 * Convert a MTBDD into a vector array.
 * 
 * The mode of the conversions refers to how the leafs are 
 * filled with the array values.
 * 
 * This can be row wise (transpose mode) or column wise.
 * 
 * Suppose M[row][col] is a matrix:
 * 
 *      M[0][0]     M[0][1]
 *      M[1][0]     M[1][1]
 * 
 * The transpose of M[row][col] = M[col][row]
 * 
 *      M[0][0]     M[1][0]
 *      M[0][1]     M[1][1]
 * 
 * Then MTBDD is column wise:
 * 
 *                          x0
 *                x1                   x1
 *          x2         x2        x2          x2
 *        M[0][0]    M[0][1]   M[1][0]     M[1][1]
 *
 * MTBDD is row wise (= transpose):
 * 
 *                          x0
 *                x1                   x1
 *          x2         x2        x2          x2
 *        M[0][0]    M[1][0]   M[0][1]     M[1][1]
 * 
 */

typedef enum {
    COLUMN_WISE_MODE,                       // f(r0,r1,c0,c1) = W[r0r1][c0c1], r,c ={ 0, 1 }
    ROW_WISE_MODE,                          // f(c0,c1,r0,r1) = W[r0r1][c0c1], r,c ={ 0, 1 }
    ALTERNATE_COLUMN_FIRST_WISE_MODE,       // f(c0,r0,c1,r1) = W[r0r1][c0c1], r,c ={ 0, 1 }
    ALTERNATE_ROW_FIRST_WISE_MODE           // f(c0,r0,c1,r1) = W[r0r1][c0c1], r,c ={ 0, 1 }
} row_column_mode_t;

/**
 * Matrix MTBDD conversion functions.
*/

typedef double VecArr_t;
typedef double MatArr_t;

int allocate_matrix_array(MatArr_t ***W_arr, int n);
int free_matrix_array(MatArr_t **W_arr, int n);

int print_vector_array(VecArr_t *v_arr, int n);
int print_matrix_array(MatArr_t **W_arr, int n);

MTBDD vector_array_to_mtbdd(VecArr_t *v_arr, int n, row_column_mode_t mode);
MTBDD matrix_array_to_mtbdd(MatArr_t **M_arr, int n, row_column_mode_t mode);

void mtbdd_to_vector_array(MTBDD v, int n, row_column_mode_t mode, VecArr_t *w);
void mtbdd_to_matrix_array(MTBDD M, int n, row_column_mode_t mode, MatArr_t **W);

/**
 * Matrix . Vector multiplication in array domain
 * 
 * Computes M.v = w for a 2^n x 2^n matrix M[row][col], and a 2^n vector v[col].
 * 
 * Results in an array of a 2^n vector w[col].
 * 
 */

void array_matrix_vector_product(MatArr_t **M_arr, VecArr_t *v_arr, int n, VecArr_t *w);

/**
 * Matrix . Matrix multiplication in array domain
 * 
 * Computes M.V = W for two 2^n x 2^n matrices M[row][col] and V[row][col].
 * 
 * Results in an array of a 2^n x 2^n matrix W[row][col].
 * 
 */

void array_matrix_matrix_product(MatArr_t **M, MatArr_t **V, int n, MatArr_t **W);
