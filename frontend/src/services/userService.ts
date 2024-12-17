import apiClient from './api';

// Define the type for user registration data
export interface UserData {
    username: string;
    email: string;
    password: string;
}

// Define the type for login credentials
export interface LoginCredentials {
    username: string;
    password: string;
}

// Register a new user
export const registerUser = (userData: UserData) => {
    return apiClient.post('/register', userData)
        .then(response => {
            const token = response.data.token;
            if (token) {
                localStorage.setItem('access_token', token);
                console.log("Token stored:", token);
            } else {
                console.error("Token is missing in response");
            }
            return response;
        })
        .catch(error => {
            console.error("Error during registration:", error);
            throw error;
        });
};

// Log in a user
export const loginUser = (credentials: LoginCredentials) => {
    return apiClient.post('/login', credentials)
        .then(response => {
            const token = response.data.access_token;

            if (token) {
                localStorage.setItem('access_token', token);
                console.log("Token stored:", token);
            } else {
                console.error("Access token is missing in the response");
            }

            return response;
        })
        .catch(error => {
            console.error("Error during login:", error);
            throw new Error('Login failed');
        });
};

// Fetch all users (authenticated route)
export const fetchUsers = () => {
    return apiClient.get('/users');
};

// Check if an email already exists
export const checkEmail = (email: string) => {
    return apiClient.post('/check-email', { email })
        .then(response => response.data.exists);
};
