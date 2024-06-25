# Exercise
### EX1: Viết 4 functions thực hiện tính thể tích của các khối sau:
- Hình lập phương $V = s^3$ (s là độ dài của cạnh) 
    - input function: s
    - output function: V
- Hình hộp chữ nhật $V = l*w*h$ (l là chiều dài, w là chiều rộng, h: là chiều cao)
    - input function: l, w, h
    - output function: V
- Hình trụ tròn: $V= \pi*r^2*h$ (r là bán kính đáy, h là chiều cao)
    - input function: r, h
    - output function: V
- Hình cầu: $V = \frac{4}{3}* \pi * r^3$ (r bán kính hình cầu)
    - input function: r
    - output function: V

NOTE: Tùy thuộc vào giá trị $\pi$ các bạn định nghĩa mà kết quả có thể sai lệch. Ví dụ tự định nghĩa $\pi = 3.14$ hoặc dùng mat.pi $\pi = 3.141592653589793$

### EX2: Viết function thực hiện đánh giá classification model bằng F1-Score. 
- ${Precision} = \dfrac{TP}{TP + FP}$
- ${Recall} = \dfrac{TP}{TP + FN}$
- ${F1-score} = 2*\dfrac{Precision*Recall}{Precision + Recall}$

- Input: function nhận 3 giá trị **tp, fp, fn**

- Output: print ra kết quả của **Precision, Recall, và F1-score**


**NOTE: Đề bài yêu cầu các điều kiện sau**
    
- Phải **kiểm tra giá trị nhận vào tp, fp, fn là type int**, nếu là type khác thì print ví dụ check fn là float, print **'fn must be int'** và thoát hàm hoặc dừng chương trình.
- Yêu cầu **tp, fp, fn phải đều lớn hơn 0**, nếu không thì print **'tp and fp and fn must be greater than zero'** và thoát hàm hoặc dừng chương trình 

### EX3: Viết function mô phỏng theo 3 activation function. 
- Binary Step Function 
$$f(x) = \left\{ \begin{array}{ll}
0 & \text{if } x < 0 \\
1 & \text{if } x \geq 0
\end{array} \right.$$


- Sigmoid Function $f(x) = \dfrac{1}{1 + e^{-x}} $

- Elu Function 
$$f(x) = \left\{ \begin{array}{ll}
\alpha (e^x - 1) & \text{if } x < 0 \\
x & \text{if } x \geq 0
\end{array} \right.$$


### EX4: Viết function lựa chọn regression loss function để tính loss:
- MAE = $ \dfrac{1}{n}∑_{i=1}^{n} |y_{i} - \hat{y}_{i}| $
- MSE = $ \dfrac{1}{n}∑_{i=1}^{n} (y_{i} - \hat{y}_{i})^2 $
- RMSE = $\sqrt{MSE}$ = $ \sqrt{\dfrac{1}{n}∑_{i=1}^{n} (y_{i} - \hat{y}_{i})^2} $
- **n** chính là **số lượng samples (num_samples)**, với **i** là mỗi sample cụ thể. Ở đây các bạn có thể hiểu là cứ mỗi **i** thì sẽ **có 1 cặp  $y_i$ là target và $\hat{y}$ là predict**.
- Input:
    - Người dùng **nhập số lượng sample (num_samples) được tạo ra (chỉ nhận integer numbers)**
    - Người dùng **nhập loss name (MAE, MSE, RMSE-(optional)) chỉ cần MAE và MSE, bạn nào muốn làm thêm RMSE đều được**.
        
- Output:
    - Print ra **loss name, sample, predict, target, loss**
        - **loss name:** là loss mà người dùng chọn
        - **sample:** là thứ tự sample được tạo ra (ví dụ num_samples=5, thì sẽ có 5 samples và mỗi sample là sample-0, sample-1, sample-2, sample-3, sample-4)
        - **predict:** là số mà model dự đoán (chỉ cần dùng random tạo random một số trong range [0,10))
        - **target:** là số target mà momg muốn mode dự đoán đúng (chỉ cần dùng random tạo random một số trong range [0,10))
        - **loss:** là kết quả khi đưa predict và target vào hàm loss 
        - **note:** ví dụ num_sample=5 thì sẽ có 5 cặp predict và target.

**Note: Các bạn lưu ý**
- Dùng **.isnumeric() method** để kiểm tra **num_samples** có hợp lệ hay không (vd: x='10', num_samples.isnumeric() sẽ trả về True ngược lại là False). Nếu **không hợp lệ print 'number of samples must be an integer number'** và dừng chương trình.
- **Dùng vòng lặp for, lặp lại num_samples lần**. **Mỗi lần dùng random modules tạo một con số ngẫu nhiên trong range [0.0, 10.0) cho predict và target**. Sau đó predict và target vào loss function và print ra kết quả mỗi lần lặp.
- Dùng **random.uniform(0,10)** để tạo ra một số ngẫu nhiên trong range [0,10)
- **Giả xử người dùng luôn nhập đúng loss name MSE, MAE, và RMSE (đơn giảng bước này để các bạn không cần check tên hợp lệ)**
- Dùng abs() để tính trị tuyệt đối ví dụ abs(-3) sẽ trả về 3
- Dùng math.sqrt() để tính căn bậc 2


### EX5: Viết các function thực hiện tam giác Pascal và dãy số Fibonacci.

**Pascal’s Triangle**
- Input: level là số lượng hàng
- Output: Print ra kết quả từng hàng theo Pascal’s Triangle

**Fibonacci Sequence**
- Input: length là độ dài của chuỗi Fibonacci
- Output: Print ra kết quả các elemet trong chuỗi Fibonacci

Note:

- Các bạn nên tìm hiểu các công thức có thể thực hiện được Pascal’s Triangle và Fibonacci
Sequence
- Nếu các bạn có kiến thức về list hoặc các kiến thức khác chưa có trong bài học thì các bạn
vẫn sử dụng được


### EX6: Viết 4 functions để ước lượng các hàm số sau.
-  Input: x (số muốn tính toán) và n (số lượng bậc muốn xấp xỉ)
- Output: Kết quả ước lượng hàm tương ứng với x. Ví dụ hàm cos(x=0) thì output = 1

**NOTE: Các bạn chú ý các điều kiện sau**
- x là radian
- n là số nguyên dương ≥ 0
- các bạn nên viết một hàm tính giai thừa riêng

### EX7: Cho một số nguyên dương n, viết phương trình đảo ngược thứ tự các vị trí trong số n. Chỉ dùng while (hay for) và những phép toán cơ bản như +, -, *, /,
%, // ...

- Input: n là một dãy số nguyên dương.
- Output: Đảo ngược vị trí các số trong n. Ví dụ input: 12345678910, output: 1987654321

**NOTE: Các bạn chú ý các điều kiện sau**
- Không được ép kiểu sang string
- Chỉ sử dụng while hoặc for loop
