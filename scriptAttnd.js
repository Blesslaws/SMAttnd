document.getElementById('attendance-form').addEventListener('submit', function(event) {
        event.preventDefault();
            
                const formData = new FormData(event.target);
                    const data = Object.fromEntries(formData.entries());

                        fetch('/submit', {
                                    method: 'POST',
                                            headers: {
                                                            'Content-Type': 'application/json'
                                            },
                                                    body: JSON.stringify(data)
                        }).then(response => response.json())
                              .then(data => {
                                          console.log('Success:', data);
                                                    loadDashboard();
                              })
                                    .catch((error) => {
                                                  console.error('Error:', error);
                                    });
});

function loadDashboard() {
        fetch('/dashboard')
                .then(response => response.json())
                        .then(data => {
                                        const ctx = document.getElementById('attendanceChart').getContext('2d');
                                                    new Chart(ctx, {
                                                                        type: 'bar',
                                                                                        data: {
                                                                                                                labels: data.labels,
                                                                                                                                    datasets: [{
                                                                                                                                                                label: 'Average Working Hours',
                                                                                                                                                                                        data: data.avg_hours,
                                                                                                                                                                                                                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                                                                                                                                                                                                                                        borderColor: 'rgba(75, 192, 192, 1)',
                                                                                                                                                                                                                                                                borderWidth: 1
                                                                                                                                    }]
                                                                                        },
                                                                                                        options: {
                                                                                                                                scales: {
                                                                                                                                                            y: {
                                                                                                                                                                                            beginAtZero: true
                                                                                                                                                            }
                                                                                                                                }
                                                                                                        }
                                                    });
                        });
}

loadDashboard();

                                                                                                                                                            }
                                                                                                                                }
                                                                                                        }
                                                                                                                                    }]
                                                                                        }
                                                    })
                        })
}
                                    })
                              })
                                            }
                        })
})