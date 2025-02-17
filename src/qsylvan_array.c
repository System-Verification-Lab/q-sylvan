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

int
allocate_matrix_array(MatArr_t ***W_arr, int n)
{
    if(n < 0)
        return 1;

    *W_arr = (MatArr_t **)malloc((1 << n) * sizeof(MatArr_t *)); // row pointers

    if(*W_arr == NULL)
        return 2;

    for(int i=0; i < (1 << n); i++) {

        (*W_arr)[i] = (MatArr_t *)malloc((1 << n) * sizeof(MatArr_t)); // all elements

        if((*W_arr)[i] == NULL)
            return 3;

        for(int j=0; j < (1 << n); j++)
            (*W_arr)[i][j] = 0.0;
    }

    return 0;
}

int
free_matrix_array(MatArr_t **W_arr, int n)
{
    if(n<0)
        return 1;

    // free all mallocs
    for(int i=0; i < (1 << n); i++) {
        free(W_arr[i]);
    }

    free(W_arr);

    return 0;
}

int
print_vector_array(VecArr_t *v_arr, int n)
{
    if(n<0)
        return 1;

    for(int row=0; row < (1 << n); row++)
        printf("v_arr[%d] = %lf\n", row, v_arr[row]);

    return 0;
}

/**
 * Print contents of the array given the element type
*/
int
print_matrix_array(MatArr_t **W_arr, int n)
{
    if(n<0)
        return 1;

    for(int row=0; row < (1 << n); row++)
        for(int column=0; column < (1 << n); column++) 
            printf("W_arr[%d][%d] = %lf\n", row, column, W_arr[row][column]);

    return 0;
}

/**
 * Utility functions:
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
 * The transpose of M[row][col] is M[col][row]
 * 
 *      M[0][0]     M[1][0]
 *      M[0][1]     M[1][1]
 * 
 * Then MTBDD is column wise:
 * 
 *                          x0
 *                x1                   x1
 *
 *        M[0][0]    M[0][1]   M[1][0]     M[1][1]
 *
 * MTBDD is row wise (= transpose):
 * 
 *                          x0
 *                x1                   x1
 *
 *        M[0][0]    M[1][0]   M[0][1]     M[1][1]
 * 
 */

MTBDD vector_array_to_mtbdd(VecArr_t *v_arr, int n, row_column_mode_t mode)
{
    if(v_arr == NULL)
        return MTBDD_ZERO;

    if(n < 0)
        return MTBDD_ZERO;
    
    if(n == 0)
        return mtbdd_double(v_arr[0]);

    if(n == 1 && (mode == COLUMN_WISE_MODE || mode == ALTERNATE_COLUMN_FIRST_WISE_MODE)) {
        return mtbdd_makenode(1, mtbdd_double(v_arr[0]), mtbdd_double(v_arr[1]));
    }

    if(n == 1 && (mode == ROW_WISE_MODE || mode == ALTERNATE_ROW_FIRST_WISE_MODE)) {

        return mtbdd_makenode(0, mtbdd_double(v_arr[0]), mtbdd_double(v_arr[1]));
    }

    // TODO: if n > 1, recursive, divide in four parts, alternate_column_first
    assert(n<2);

    return MTBDD_ZERO;
}

MTBDD matrix_array_to_mtbdd(MatArr_t **M_arr, int n, row_column_mode_t mode)
{
    if(M_arr == NULL)
        return MTBDD_ZERO;

    if(n < 0)
        return MTBDD_ZERO;

    if(n == 0) 
        return mtbdd_double(M_arr[0][0]);

    if(n == 1 && (mode == COLUMN_WISE_MODE || mode == ALTERNATE_COLUMN_FIRST_WISE_MODE)) {

        MTBDD column0 = mtbdd_makenode(1, mtbdd_double(M_arr[0][0]), mtbdd_double(M_arr[1][0]));
        MTBDD column1 = mtbdd_makenode(1, mtbdd_double(M_arr[0][1]), mtbdd_double(M_arr[1][1]));

        return mtbdd_makenode(0, column0, column1);
    }

    if(n == 1 && (mode == ROW_WISE_MODE || mode == ALTERNATE_ROW_FIRST_WISE_MODE)) {

        MTBDD row0 = mtbdd_makenode(1, mtbdd_double(M_arr[0][0]), mtbdd_double(M_arr[0][1]));
        MTBDD row1 = mtbdd_makenode(1, mtbdd_double(M_arr[1][0]), mtbdd_double(M_arr[1][1]));

        return mtbdd_makenode(0, row0, row1);
    }

    // TODO: if n > 1, recursive, divide in four parts
    assert(n<2);

    return MTBDD_ZERO;
}

void mtbdd_to_vector_array(MTBDD v, int n, row_column_mode_t mode, VecArr_t *w)
{
    MatArr_t **W_arr = NULL;
    allocate_matrix_array(&W_arr, n);

    mtbdd_to_matrix_array(v, n, mode, W_arr);

    for(int row=0; row < (1 << n); row++)
        w[row] = W_arr[row][0];

    free_matrix_array(W_arr, n);

    return;
}

void mtbdd_to_matrix_array(MTBDD M, int n, row_column_mode_t mode, MatArr_t **W) // TODO: refactor to make more compact
{
    //
    // The leaf can be reached by the composite row * 2^n + column
    //
    // Example: 
    //
    //   row = 3, column = 5, n = 3. 
    //
    // That corresponds to a matrix of 2^3 x 2^3 = 8 x 8, or in C: "MatArr_t W[8][8]". 
    //
    // The row and column index = {0,1,..,7} = {0, ..., ((2^3)-1)}, W[row][column].
    //
    //  W[3][5] = W[011][100] = M[011100]
    //
    // By starting traversing through M from the root, first go to node 011. That is 2^3 deep.
    //
    // Under this node you find a mtbdd with depth 2^3 with leafs corresponding to W[][column].
    //
    // So, traversing further on with node[100] = getlow(getlow(gethigh(node))) you reach the leaf
    //
    // with as value equal to W[3][5].
    //
    //  W[3][5] = W[011][100] = leaf(node[100]) = leaf(M[011100])
    //

    if(M == MTBDD_ZERO)
        return;

    if(n <= 0)
        return;

    // f(c0,r0,c1,r1) = W[r0r1][c0c1] or f(r0,c0,r1,c1) = W[r0r1][c0c1]
    if(mode == ALTERNATE_COLUMN_FIRST_WISE_MODE || mode == ALTERNATE_ROW_FIRST_WISE_MODE) {

        for(int index=0; index < (1 << (2 * n)); index++) {
            
            MTBDD node = M;
            
            bool turn_for_column = true;

            int row = 0;
            int column = 0;

            int bit_row = (1 << (n-1)) - 1;
            int bit_column = (1 << (n-1)) - 1;

            for(int bit=((2 * n) - 1); bit >= 0; bit--) {

                if((index & (1 << bit)) == 0) {

                    if(mtbdd_getlow(node) != MTBDD_ZERO && mtbdd_isleaf(node) == 0) 
                        node = mtbdd_getlow(node);

                    if(turn_for_column) {
                        column += (0 << bit_column); // TODO: can be removed
                        bit_column -= 1;
                        turn_for_column = false;
                    }

                    else {
                        row += (0 << bit_row); // TODO: can be removed
                        bit_row -= 1;
                        turn_for_column = true;
                    }

                    //printf("node = %ld, index = %d, getlow -> bit=%d, row=%d, column=%d\n", node, index, bit, row, column);

                }
                else {

                    if(mtbdd_gethigh(node) != MTBDD_ZERO && mtbdd_isleaf(node) == 0) 
                        node = mtbdd_gethigh(node);

                    if(turn_for_column) {
                        column += (1 << bit_column);
                        bit_column -= 1;
                        turn_for_column = false;
                    }

                    else {
                        row += (1 << bit_row);
                        bit_row -= 1;
                        turn_for_column = true;
                    }

                    //printf("node = %ld, index = %d, getlow -> bit=%d, row=%d, column=%d\n", node, index, bit, row, column);

                }
            }

            //printf("row=%d, column=%d\n", row, column);

            if(mode == ALTERNATE_COLUMN_FIRST_WISE_MODE)
                W[row][column] = mtbdd_getdouble(node);

            if(mode == ALTERNATE_ROW_FIRST_WISE_MODE)
                W[column][row] = mtbdd_getdouble(node);
        }

        return;
    }

    // f(r0,r1,c0,c1) or f(c0,c1,r0,r1) 
    for(int row=0; row < (1 << n); row++) {

        MTBDD node = M;

        // Traverse through M from root to row node
        for(int bit=(n-1); bit >= 0; bit--) {

            if((row & (1 << bit)) == 0) {
                if(mtbdd_getlow(node) != MTBDD_ZERO && mtbdd_isleaf(node) == 0) 
                    node = mtbdd_getlow(node);
                
                //printf("row=%d getlow()\n", row);
            }
            else {
                if(mtbdd_gethigh(node) != MTBDD_ZERO && mtbdd_isleaf(node) == 0) 
                    node = mtbdd_gethigh(node);
                
                //printf("row=%d gethigh()\n", row);
            }
        }

        MTBDD row_node = node;

        for(int column=0; column < (1 << n); column++) {

            node = row_node;

            // Traverse through M from node to column node
            for(int bit=(n-1); bit >= 0; bit--) {

                if((column & (1 << bit)) == 0) {
                    if(mtbdd_getlow(node) != MTBDD_ZERO && mtbdd_isleaf(node) == 0) 
                        node = mtbdd_getlow(node);
                    
                    //printf("column=%d getlow()\n", column);
                }
                else {
                    if(mtbdd_gethigh(node) != MTBDD_ZERO && mtbdd_isleaf(node) == 0) 
                        node = mtbdd_gethigh(node);
                    
                    //printf("column=%d gethigh()\n", column);
                }
            }

            if(mode == COLUMN_WISE_MODE)
                W[row][column] = mtbdd_getdouble(node);

            if(mode == ROW_WISE_MODE)
                W[column][row] = mtbdd_getdouble(node);
        }
    }

    return;
}

/**
 * Matrix . Vector multiplication in MTBDD domain
 * 
 * Computes M.v = w for a 2^n x 2^n matrix M[row][col], and a 2^n vector v[col].
 * 
 * Results in an array of a 2^n vector w[col].
 * 
 */
void array_matrix_vector_product(MatArr_t **M, VecArr_t *v, int n, VecArr_t *w)
{
    // Convert to MTBDD
    MTBDD M_col = matrix_array_to_mtbdd(M, n, COLUMN_WISE_MODE);
    MTBDD v_row = vector_array_to_mtbdd(v, n, ROW_WISE_MODE);

    // Multiply in MTBDD domain
    MTBDD w_col = mtbdd_matvec_mult_alt(M_col, v_row, n); // TODO: take none alt

    mtbdd_to_vector_array(w_col, n, COLUMN_WISE_MODE, w);

    return;
}

/**
 * Matrix . Matrix multiplication in MTBDD domain
 * 
 * Computes M.V = W for two 2^n x 2^n matrices M[row][col] and V[row][col].
 * 
 * Results in an array of a 2^n x 2^n matrix W[row][col]. 
 * 
 */
void array_matrix_matrix_product(MatArr_t **M1, MatArr_t **M2, int n, MatArr_t **W)
{
    // Convert to MTBDD
    MTBDD M1_col = matrix_array_to_mtbdd(M1, n, COLUMN_WISE_MODE);
    MTBDD M2_row = matrix_array_to_mtbdd(M2, n, ROW_WISE_MODE);

    // Multiply in MTBDD domain
    MTBDD W_col = mtbdd_matmat_mult_alt(M1_col, M2_row, n); // TODO: take none alt

    mtbdd_to_matrix_array(W_col, n, COLUMN_WISE_MODE, W);
    
    return;
}


