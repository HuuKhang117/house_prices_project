<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hệ Thống Dự Đoán Giá Nhà</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
        }
        
        .card {
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border: none;
            margin-bottom: 20px;
        }
        
        .card-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px 15px 0 0 !important;
            padding: 20px;
            font-weight: bold;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            padding: 10px 30px;
            border-radius: 25px;
            transition: all 0.3s;
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        
        .form-control, .form-select {
            border-radius: 10px;
            padding: 12px;
        }
        
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        
        .prediction-result {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .upload-area {
            border: 3px dashed #667eea;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            background: #f8f9fa;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .upload-area:hover {
            background: #e9ecef;
            border-color: #764ba2;
        }
        
        .table-container {
            max-height: 500px;
            overflow-y: auto;
        }
        
        .btn-secondary {
            border-radius: 25px;
            padding: 8px 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12">
            <div class="card">
                    <div class="card-header">
                        <h1 class="mb-0"><i class="fas fa-home"></i> Hệ Thống Dự Đoán Giá Nhà</h1>
                        <p class="mb-0 mt-2">Nhập thông tin để dự đoán giá nhà hoặc tải lên file dữ liệu để phân tích</p>
                    </div>
                    <div class="card-body p-4">
                        
                        <!-- Prediction Form -->
                        <div class="card mb-4">
                            <div class="card-header bg-info text-white">
                                <h3><i class="fas fa-calculator"></i> Dự Đoán Giá Nhà Đơn Lẻ</h3>
                            </div>
                            <div class="card-body">
                                <form id="predictionForm">
                                    <div class="row g-3">
                                        <div class="col-md-3">
                                            <label class="form-label"><i class="fas fa-ruler"></i> Diện tích (m²)</label>
                                            <input type="number" class="form-control" id="area" step="0.01" required>
                                        </div>
                                        <div class="col-md-3">
                                            <label class="form-label"><i class="fas fa-bed"></i> Số phòng ngủ</label>
                                            <input type="number" class="form-control" id="bedrooms" min="1" max="10" required>
                                        </div>
                                        <div class="col-md-3">
                                            <label class="form-label"><i class="fas fa-bath"></i> Số phòng tắm</label>
                                            <input type="number" class="form-control" id="bathrooms" step="0.1" min="1" required>
                                        </div>
                                        <div class="col-md-3">
                                            <label class="form-label"><i class="fas fa-calendar"></i> Tuổi nhà (năm)</label>
                                            <input type="number" class="form-control" id="age" min="0" required>
                                        </div>
                                    </div>
                                    <div class="row mt-4">
                                        <div class="col-12 text-center">
                                            <button type="submit" class="btn btn-primary btn-lg">
                                                <i class="fas fa-search"></i> Dự Đoán Giá
                                            </button>
                                        </div>
                                    </div>
                                </form>
                                
                                <div id="predictionResult" style="display: none;">
                                <div class="prediction-result">
                                        Giá nhà dự đoán: <span id="predictedPrice"></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
<!-- Charts after prediction -->
<div id="analysisCharts" style="display: none; margin-top: 30px;">
    <h3 class="text-white mb-3"><i class="fas fa-chart-bar"></i> Biểu Đồ Phân Tích Dữ Liệu</h3>
    <div class="row">
        <div class="col-md-4 mb-4">
            <div class="chart-container">
                <img id="chartImg1" src="" alt="Biểu đồ 1" class="img-fluid rounded">
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="chart-container">
                <img id="chartImg2" src="" alt="Biểu đồ 2" class="img-fluid rounded">
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="chart-container">
                <img id="chartImg3" src="" alt="Biểu đồ 3" class="img-fluid rounded">
            </div>
        </div>
    </div>
</div>


                        <!-- Upload or Sample Data -->
                        <div class="card mb-4">
                            <div class="card-header bg-success text-white">
                                <h3><i class="fas fa-chart-line"></i> Phân Tích Dữ Liệu</h3>
                            </div>
                            <div class="card-body">
                                <div class="row mb-4">
                                    <div class="col-md-6">
                                        <div class="upload-area" onclick="document.getElementById('fileInput').click()">
                                            <i class="fas fa-cloud-upload-alt fa-3x mb-3"></i>
                                            <h4>Tải lên file dữ liệu</h4>
                                            <p class="text-muted">CSV, XLS, XLSX</p>
                                            <input type="file" id="fileInput" accept=".csv,.xls,.xlsx" style="display: none;">
                                        </div>
                                    </div>
                                    <div class="col-md-6 text-center">
                                        <button class="btn btn-secondary btn-lg mt-4" onclick="useSampleData()">
                                            <i class="fas fa-database"></i> Sử dụng dữ liệu mẫu
                                        </button>
                                    </div>
                                </div>
                                
                                <div id="uploadStatus" class="alert" style="display: none;"></div>
                            </div>
                        </div>
                        
                        <!-- Charts Section -->
                        <div id="chartsSection" style="display: none;">
                        <div class="row">
                                <div class="col-md-12">
                                    <h3 class="text-white mb-3"><i class="fas fa-chart-bar"></i> Biểu Đồ Phân Tích</h3>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-6 mb-4">
                                    <div class="chart-container">
                                        <div id="chart1"></div>
                                    </div>
                                </div>
                                <div class="col-md-6 mb-4">
                                    <div class="chart-container">
                                        <div id="chart2"></div>
                                    </div>
                                </div>
                                <div class="col-md-6 mb-4">
                                    <div class="chart-container">
                                        <div id="chart3"></div>
                                    </div>
                                </div>
                                <div class="col-md-6 mb-4">
                                    <div class="chart-container">
                                        <div id="chart4"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Data Table -->
                        <div id="dataTableSection" style="display: none;">
                            <div class="card mb-4">
                                <div class="card-header bg-primary text-white">
                                    <h3><i class="fas fa-table"></i> Dữ Liệu Đã Phân Tích</h3>
                                </div>
                                <div class="card-body">
                                    <div class="table-container">
                                        <table class="table table-striped table-hover">
                                            <thead id="tableHead"></thead>
                                            <tbody id="tableBody"></tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Handle prediction form submission
        document.getElementById('predictionForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const area = parseFloat(document.getElementById('area').value);
            const bedrooms = parseInt(document.getElementById('bedrooms').value);
            const bathrooms = parseFloat(document.getElementById('bathrooms').value);
            const age = parseInt(document.getElementById('age').value);
            
            try {
                const response = await fetch('/predict_with_analysis', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ area, bedrooms, bathrooms, age })
                });
                
                const result = await response.json();
                
                if (result.status === 'success') {
                    // ✅ Hiển thị giá nhà dự đoán
                    document.getElementById('predictedPrice').textContent =
            result.prediction_formatted || 
            result.prediction.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' });
        document.getElementById('predictionResult').style.display = 'block';

        // ✅ Hiển thị biểu đồ phân tích nếu có
        if (result.charts) {
            displayData(
                [{
                    area,
                    bedrooms,
                    bathrooms,
                    age,
                    predicted_price: result.prediction
                }],
                result.charts
            );
        }

                } else {
                    alert('Lỗi: ' + result.message);
                }
            } catch (error) {
                alert('Lỗi kết nối: ' + error.message);
            }
        });
        


        
        // Handle file upload
        document.getElementById('fileInput').addEventListener('change', async function(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            const formData = new FormData();
            formData.append('file', file);
            
            try {
                const response = await fetch('/upload_file', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (result.status === 'success') {
                    showStatus('Tải file thành công! Đang xử lý...', 'success');
                    displayData(result.data, result.charts);
                } else {
                    showStatus('Lỗi: ' + result.message, 'danger');
                }
            } catch (error) {
                showStatus('Lỗi: ' + error.message, 'danger');
            }
        });
        
        // Use sample data
        async function useSampleData() {
            showStatus('Đang tạo dữ liệu mẫu...', 'info');
            
            try {
                const response = await fetch('/use_sample_data', {
                    method: 'POST'
                });
                const result = await response.json();
                
                if (result.status === 'success') {
                    showStatus('Đã tạo dữ liệu mẫu thành công!', 'success');
                    displayData(result.data, result.charts);
                } else {
                    showStatus('Lỗi: ' + result.message, 'danger');
                }
            } catch (error) {
                showStatus('Lỗi: ' + error.message, 'danger');
            }
        }
        
        function showStatus(message, type) {
            const statusDiv = document.getElementById('uploadStatus');
            statusDiv.textContent = message;
            statusDiv.className = 'alert alert-' + type;
            statusDiv.style.display = 'block';
        }
        
        function displayData(data, charts) {
            // Display charts
            if (charts) {
                if (charts.price_distribution) {
                    Plotly.newPlot('chart1', JSON.parse(charts.price_distribution));
                }
                if (charts.area_price) {
                    Plotly.newPlot('chart2', JSON.parse(charts.area_price));
                }
                if (charts.bedrooms_price) {
                    Plotly.newPlot('chart3', JSON.parse(charts.bedrooms_price));
                }
                if (charts.feature_correlation) {
                    Plotly.newPlot('chart4', JSON.parse(charts.feature_correlation));
                }
                
                document.getElementById('chartsSection').style.display = 'block';
            }
            
            // Display data table
            if (data && data.length > 0) {
                const firstRow = data[0];
                const headers = Object.keys(firstRow);
                
                let headerRow = '<tr>';
                headers.forEach(header => {
                    headerRow += `<th>${translateHeader(header)}</th>`;
                });
                headerRow += '</tr>';
                document.getElementById('tableHead').innerHTML = headerRow;
                
                let bodyRows = '';
                data.forEach(row => {
                    bodyRows += '<tr>';
                    headers.forEach(header => {
                        bodyRows += `<td>${formatValue(row[header])}</td>`;
                    });
                    bodyRows += '</tr>';
                });
                document.getElementById('tableBody').innerHTML = bodyRows;
                
                document.getElementById('dataTableSection').style.display = 'block';
            }
        }
        
        function translateHeader(header) {
            const translations = {
                'area': 'Diện tích (m²)',
                'bedrooms': 'Phòng ngủ',
                'bathrooms': 'Phòng tắm',
                'age': 'Tuổi (năm)',
                'price': 'Giá thực tế (triệu)',
                'predicted_price': 'Giá dự đoán (triệu)'
                };
            return translations[header] || header;
        }
        
        function formatValue(value) {
            if (typeof value === 'number') {
                return value.toLocaleString('vi-VN');
            }
            return value;
        }
        
        // Train model on page load
        window.addEventListener('load', async function() {
            try {
                const response = await fetch('/train_model', {
                    method: 'POST'
                });
                const result = await response.json();
                if (result.status === 'success') {
                    console.log('Model đã được train thành công');
                }
            } catch (error) {
                console.error('Lỗi train model:', error);
            }
        });
    </script>
</body>
</html>

