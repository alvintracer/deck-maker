---
type: project
date: 2026-06-23
status: draft
tags: [wallet, crypto, non-custodial, cross-chain]
---

# Took Wallet Service Features and Vision

# Traverse Wallet (took) Overview

`took` is a non-custodial cross-chain wallet designed to combine security, regulatory compliance, and usability. It supports EVM chains, Solana, Bitcoin, and Tron through a unified interface.

## Core Features

- **Multi-Wallet Slots**: Manage multiple wallet types (MPC, MetaMask, Rabby, SAR) in one app with cross-chain aggregation.
- **Self-Administered Recovery (SAR)**: Uses SSS and cloud KMS for recovery via personal identifiers without seed phrases.
- **Phone-Based Transfers**: Send stablecoins using only phone numbers; supports non-users via smart escrow.
- **Gasless Transactions**: Relayer contracts enable fee payment in stablecoins without native tokens.
- **Proximity Payments**: QR-based "툭 주기/받기" for offline transfers completed in ~5 seconds with automatic network matching.
- **Exchange Integration**: Direct withdrawals from Korean exchanges (Bithumb, Coinone) with Travel Rule optimizations.
- **Automated KYT/AML**: Real-time on-chain risk detection to block sanctioned or high-risk addresses.

This specification serves as the primary reference for product vision, compliance goals, and UX targets.
